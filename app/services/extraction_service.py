# app/services/extraction_service.py
from app.models.extraction_models import ExtractionRequest, ExtractionResponse
from automate_linkedin_posts.crews.extraction_crew.extraction_crew import ExtractionCrew
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ExtractionService:
    def __init__(self):
        self._executor = ThreadPoolExecutor()

    async def extract_content(self, request: ExtractionRequest) -> ExtractionResponse:
        # Create crew
        crew = ExtractionCrew().crew()
        
        try:
            # Prepare inputs for the crew
            inputs = {
                "url": str(request.url)
            }
            
            if request.options:
                inputs.update(request.options)
            
            # Run kickoff in a thread pool to avoid blocking
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(
                self._executor,
                lambda: crew.kickoff(inputs=inputs)
            )
            
            # Parse the result - assuming result.raw contains the extracted content
            return ExtractionResponse(
                extracted_content=result.raw,
                metadata={
                    "url": str(request.url),
                    "source": "extraction_crew"
                }
            )
        except Exception as e:
            raise Exception(f"Error extracting content: {str(e)}")
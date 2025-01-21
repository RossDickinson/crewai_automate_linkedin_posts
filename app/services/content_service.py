from app.models.content_models import ContentRequest, ContentResponse
from app.services.writing_style_service import WritingStyleService
from automate_linkedin_posts.crews.content_crew.content_crew import ContentCrew
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ContentService:
    def __init__(self):
        self._executor = ThreadPoolExecutor()
        self._writing_style_service = WritingStyleService()

    async def generate_content(self, request: ContentRequest) -> ContentResponse:
        # Create crew
        crew = ContentCrew().crew()
        
        try:
            # Get writing style text
            writing_style_text = self._writing_style_service.get_style_text(
                request.writing_style_id
            )
            
            # Prepare inputs for the crew
            inputs = {
                "extracted_info": request.extracted_info,
                "writing_style_text": writing_style_text,
                "target_audience": request.target_audience
            }
            
            # Run kickoff in a thread pool to avoid blocking
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(
                self._executor,
                lambda: crew.kickoff(inputs=inputs)
            )
            
            return ContentResponse(
                content=result.raw,
                metadata={
                    "writing_style_id": request.writing_style_id,
                    "target_audience": request.target_audience
                }
            )
        except Exception as e:
            raise Exception(f"Error generating content: {str(e)}")
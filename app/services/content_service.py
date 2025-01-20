# app/services/content_service.py
from app.models.content_models import ContentRequest, ContentResponse
from automate_linkedin_posts.crews.content_crew.content_crew import ContentCrew
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ContentService:
    def __init__(self):
        self._executor = ThreadPoolExecutor()

    async def generate_content(self, request: ContentRequest) -> ContentResponse:
        # Create crew
        crew = ContentCrew().crew()
        
        try:
            # Prepare inputs for the crew
            inputs = {
                "url": str(request.url),
                "extracted_info": request.extracted_info or {}
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
                    "url": str(request.url),
                    "source": "content_crew"
                }
            )
        except Exception as e:
            raise Exception(f"Error generating content: {str(e)}")
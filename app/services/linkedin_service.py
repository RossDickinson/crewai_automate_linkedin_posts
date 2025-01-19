from app.models.linkedin_models import LinkedInPostRequest, LinkedInPostResponse
from automate_linkedin_posts.main import LinkedInContentFlow
import asyncio
from concurrent.futures import ThreadPoolExecutor

class LinkedInService:
    def __init__(self):
        self._executor = ThreadPoolExecutor()

    async def generate_post(self, request: LinkedInPostRequest) -> LinkedInPostResponse:
        flow = LinkedInContentFlow()
        flow.state.url = str(request.url)
        flow.state.question = request.question
        
        try:
            # Run kickoff in a thread pool to avoid blocking
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(
                self._executor,
                flow.kickoff
            )
            
            return LinkedInPostResponse(
                post_content=flow.state.final_post,
                metadata={
                    "extracted_info": getattr(flow.state, 'extracted_info', None),
                    "research_data": getattr(flow.state, 'research_data', None)
                }
            )
        except Exception as e:
            raise Exception(f"Error generating LinkedIn post: {str(e)}")
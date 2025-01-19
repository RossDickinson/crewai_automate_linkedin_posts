# app/routers/linkedin_router.py
from fastapi import APIRouter, HTTPException
from app.services.linkedin_service import LinkedInService
from app.models.linkedin_models import LinkedInPostRequest, LinkedInPostResponse

# Create the router instance
router = APIRouter()
linkedin_service = LinkedInService()

@router.post("/generate-post", response_model=LinkedInPostResponse)
async def generate_linkedin_post(request: LinkedInPostRequest):
    try:
        result = await linkedin_service.generate_post(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Make sure router is available for import
__all__ = ['router']
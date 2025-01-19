from fastapi import APIRouter
from app.routers import linkedin_router, flows_router

api_router = APIRouter()

api_router.include_router(linkedin_router.router, prefix="/linkedin", tags=["linkedin"])
api_router.include_router(flows_router.router, prefix="/flows", tags=["flows"])

# app/routers/linkedin_router.py
from fastapi import APIRouter, HTTPException
from app.services.linkedin_service import LinkedInService
from app.models.linkedin_models import LinkedInPostRequest, LinkedInPostResponse

router = APIRouter()
linkedin_service = LinkedInService()

@router.post("/generate-post", response_model=LinkedInPostResponse)
async def generate_linkedin_post(request: LinkedInPostRequest):
    try:
        result = await linkedin_service.generate_post(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
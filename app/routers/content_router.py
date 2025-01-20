# app/routers/content_router.py
from fastapi import APIRouter, HTTPException
from app.services.content_service import ContentService
from app.models.content_models import ContentRequest, ContentResponse

router = APIRouter()
content_service = ContentService()

@router.post("/generate", response_model=ContentResponse)
async def generate_content(request: ContentRequest):
    """
    Generate content from a URL using the content crew.
    """
    try:
        result = await content_service.generate_content(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Make sure router is available for import
__all__ = ['router']
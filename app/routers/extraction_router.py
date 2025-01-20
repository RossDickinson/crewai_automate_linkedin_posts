# app/routers/extraction_router.py
from fastapi import APIRouter, HTTPException
from app.services.extraction_service import ExtractionService
from app.models.extraction_models import ExtractionRequest, ExtractionResponse

router = APIRouter()
extraction_service = ExtractionService()

@router.post("/extract", response_model=ExtractionResponse)
async def extract_content(request: ExtractionRequest):
    """
    Extract content from a URL using the extraction crew.
    """
    try:
        result = await extraction_service.extract_content(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
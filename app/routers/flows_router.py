# app/routers/flows_router.py
from fastapi import APIRouter, HTTPException
from app.services.flow_service import FlowService
from app.models.flow_models import FlowRequest, FlowResponse

# Create the router instance
router = APIRouter()
flow_service = FlowService()

@router.post("/execute", response_model=FlowResponse)
async def execute_flow(request: FlowRequest):
    try:
        result = await flow_service.execute_flow(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Make sure router is available for import
__all__ = ['router']
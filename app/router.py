# app/router.py
from fastapi import APIRouter
from app.routers import linkedin_router, flows_router, content_router, extraction_router

# Create main API router
api_router = APIRouter()

# Include all sub-routers
api_router.include_router(
    linkedin_router,
    prefix="/linkedin",
    tags=["linkedin"]
)

api_router.include_router(
    flows_router,
    prefix="/flows",
    tags=["flows"]
)

api_router.include_router(
    content_router,
    prefix="/content",
    tags=["content"]
)

api_router.include_router(
    extraction_router,
    prefix="/extraction",
    tags=["extraction"]
)

# Make sure router is available for import
__all__ = ['api_router']
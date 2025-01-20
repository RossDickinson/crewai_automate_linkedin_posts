# app/routers/__init__.py
from app.routers.linkedin_router import router as linkedin_router
from app.routers.flows_router import router as flows_router
from app.routers.content_router import router as content_router
from app.routers.extraction_router import router as extraction_router

__all__ = ['linkedin_router', 'flows_router', 'content_router', 'extraction_router']
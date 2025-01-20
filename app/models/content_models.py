# app/models/content_models.py
from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict, Any

class ContentRequest(BaseModel):
    url: HttpUrl
    extracted_info: Optional[Dict[str, Any]] = None

class ContentResponse(BaseModel):
    content: str
    metadata: Optional[Dict[str, Any]] = None
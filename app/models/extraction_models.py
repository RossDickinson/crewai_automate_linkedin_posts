# app/models/extraction_models.py
from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict, Any

class ExtractionRequest(BaseModel):
    url: HttpUrl
    options: Optional[Dict[str, Any]] = None

class ExtractionResponse(BaseModel):
    extracted_content: Any
    metadata: Optional[Dict[str, Any]] = None
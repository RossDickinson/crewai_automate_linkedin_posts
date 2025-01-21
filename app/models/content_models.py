from pydantic import BaseModel
from typing import Optional, Dict, Any

class ContentRequest(BaseModel):
    extracted_info: Dict[str, Any]
    writing_style_id: str
    target_audience: str

class ContentResponse(BaseModel):
    content: str
    metadata: Optional[Dict[str, Any]] = None
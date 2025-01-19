from pydantic import BaseModel, HttpUrl
from typing import Optional, Any

class LinkedInPostRequest(BaseModel):
    url: HttpUrl
    question: Optional[str] = None

class LinkedInPostResponse(BaseModel):
    post_content: str
    metadata: Optional[dict] = None
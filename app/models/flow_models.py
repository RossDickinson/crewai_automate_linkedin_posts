from pydantic import BaseModel
from typing import Optional, Dict, Any

class FlowRequest(BaseModel):
    flow_name: str
    inputs: Dict[str, Any]
    config: Optional[Dict[str, Any]] = None

class FlowResponse(BaseModel):
    flow_id: str
    status: str
    result: Optional[Any] = None
    error: Optional[str] = None
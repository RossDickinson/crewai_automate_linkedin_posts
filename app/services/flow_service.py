from app.models.flow_models import FlowRequest, FlowResponse
import uuid
from typing import Dict, Type
from automate_linkedin_posts.main import LinkedInContentFlow

class FlowService:
    def __init__(self):
        self.flows: Dict[str, Type] = {
            "linkedin_content": LinkedInContentFlow
            # Add more flows here as they are created
        }
    
    async def execute_flow(self, request: FlowRequest) -> FlowResponse:
        flow_class = self.flows.get(request.flow_name)
        if not flow_class:
            raise ValueError(f"Flow '{request.flow_name}' not found")
            
        flow = flow_class()
        flow_id = str(uuid.uuid4())
        
        try:
            # Set initial state based on inputs
            for key, value in request.inputs.items():
                setattr(flow.state, key, value)
            
            result = await flow.kickoff()
            
            return FlowResponse(
                flow_id=flow_id,
                status="completed",
                result=result
            )
        except Exception as e:
            return FlowResponse(
                flow_id=flow_id,
                status="failed",
                error=str(e)
            )
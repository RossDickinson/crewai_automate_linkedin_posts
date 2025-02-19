# app/main.py
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Import main router
from app.router import api_router

# Load environment variables
load_dotenv()

app = FastAPI(
    title="LinkedIn Automation API",
    description="API for automating LinkedIn content creation and other flows",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the main router
app.include_router(api_router)

if __name__ == "__main__":
    # Get port from environment variable or default to 8000
    port = int(os.getenv("PORT", 8000))
    
    # Run the FastAPI application
    uvicorn.run(
        "app.main:app",  # Use the full module path
        host="0.0.0.0",
        port=port,
        reload=True,
        reload_dirs=[str(project_root)]  # Watch the entire project directory
    )
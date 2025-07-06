from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid
from datetime import datetime


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")


# Define Models
class Project(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    category: str
    technologies: List[str] = []
    github_url: Optional[str] = None
    google_drive_url: Optional[str] = None
    demo_url: Optional[str] = None
    image_url: Optional[str] = None
    featured: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ProjectCreate(BaseModel):
    title: str
    description: str
    category: str
    technologies: List[str] = []
    github_url: Optional[str] = None
    google_drive_url: Optional[str] = None
    demo_url: Optional[str] = None
    image_url: Optional[str] = None
    featured: bool = False

class StatusCheck(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class StatusCheckCreate(BaseModel):
    client_name: str

# Add your routes to the router instead of directly to app
@api_router.get("/")
async def root():
    return {"message": "Owen Roth's Portfolio API"}

# Project endpoints
@api_router.get("/projects", response_model=List[Project])
async def get_projects():
    projects = await db.projects.find().to_list(1000)
    return [Project(**project) for project in projects]

@api_router.get("/projects/{project_id}", response_model=Project)
async def get_project(project_id: str):
    project = await db.projects.find_one({"id": project_id})
    if project:
        return Project(**project)
    return {"error": "Project not found"}

@api_router.post("/projects", response_model=Project)
async def create_project(project_data: ProjectCreate):
    project_dict = project_data.dict()
    project_obj = Project(**project_dict)
    await db.projects.insert_one(project_obj.dict())
    return project_obj

@api_router.get("/projects/category/{category}", response_model=List[Project])
async def get_projects_by_category(category: str):
    projects = await db.projects.find({"category": category}).to_list(1000)
    return [Project(**project) for project in projects]

# Status check endpoints (keeping existing functionality)
@api_router.post("/status", response_model=StatusCheck)
async def create_status_check(input: StatusCheckCreate):
    status_dict = input.dict()
    status_obj = StatusCheck(**status_dict)
    _ = await db.status_checks.insert_one(status_obj.dict())
    return status_obj

@api_router.get("/status", response_model=List[StatusCheck])
async def get_status_checks():
    status_checks = await db.status_checks.find().to_list(1000)
    return [StatusCheck(**status_check) for status_check in status_checks]

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=[
        "*",  # For development
        "https://*.github.io",  # For GitHub Pages
        "https://*.githubusercontent.com",  # For GitHub Pages custom domains
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()

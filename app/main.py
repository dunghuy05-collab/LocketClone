from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.routers.health import router as health_router

app = FastAPI(title=settings.app_name)

app.include_router(health_router, prefix="/api/v1", tags=["health"])

@app.get("/")

def root():
    return {"message": "Welcome to Locket Clone API"}

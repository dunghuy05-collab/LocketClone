from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.routers.health import router as health_router
from app.api.v1.routers.users import router as user_router
from app.api.v1.routers.auth import router as auth_router
from app.api.v1.routers.photos import router as photos_router
from app.api.v1.routers.friends import router as friends_router
from app.api.v1.routers.notifications import router as notifications_router



app = FastAPI(title=settings.app_name)

app.include_router(health_router, prefix="/api/v1", tags=["health"])
app.include_router(user_router, prefix='/api/v1',tags=['users'])
app.include_router(auth_router, prefix='/api/v1',tags=['auth'])
app.include_router(photos_router, prefix='/api/v1',tags=['photos'])
app.include_router(friends_router,prefix='/api/v1',tags=['friends'])
app.include_router(notifications_router,prefix='/api/v1',tags=['notifications'])

@app.get("/")

def root():
    return {"message": "Welcome to Locket Clone API"}

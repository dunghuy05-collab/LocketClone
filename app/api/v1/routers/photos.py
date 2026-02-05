from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from schemas.photo import PhotoCreate, PhotoOut
from services.photo_service import create_photo, list_photos

router = APIRouter()

@router.post("/photos/", response_model=PhotoOut)
def create_photo_endpoint(photo_in: PhotoCreate, db: Session = Depends(get_db)):
    return create_photo(db, photo_in)

@router.get("/photos/", response_model=list[PhotoOut])
def list_photos_endpoint(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return list_photos(db, skip=skip, limit=limit)
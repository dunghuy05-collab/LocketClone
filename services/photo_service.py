from sqlalchemy.orm import Session

from models import Photo
from schemas.photo import PhotoCreate

def create_photo(db: Session, photo_in: PhotoCreate):
    photo = Photo(
        user_id= photo_in.user_id,
        image_url=photo_in.image_url,
        caption=photo_in.caption,
    )
    db.add(photo)
    db.commit()
    db.refresh(photo)
    return photo

def list_photos(db : Session, skip: int = 0, limit: int = 20):
    return db.query(Photo).offset(skip).limit(limit).all()
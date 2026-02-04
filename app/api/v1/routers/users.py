from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from services.user_service import UserCreate, UserOut
from services.user_service import create_user, get_user_by_email, list_users

router = APIRouter()

@router.post("/users/", response_model= UserOut)

def create_user_endpoint(
    user_in: UserCreate,
    db: Session=Depends(get_db)
):
    existing = get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db,user_in)

@router.get('/users/', response_model=list[UserOut])

def list_user_endpoint(skip:int=0,
                       limit:int=100,
                       db:Session=Depends(get_db)
                       ):
    return list_users(db, skip=skip, limit=limit)
    
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.sercurity import create_access_token
from schemas.user import UserLogin
from services.user_service import authenticate_user

router = APIRouter()
@router.post("/auth/login")

def login(user_in: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_in.email, user_in.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub":str(user.id)})
    return {"access_token":token, "token_type": "bearer}
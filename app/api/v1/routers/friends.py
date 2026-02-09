from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from schemas.friend import FriendCreate, FriendOut
from services.friend_service import send_request, accept_request,list_friends

router = APIRouter()

@router.post("/friends/request", response_model=FriendOut)
def request_friend(friend_in: FriendCreate, db: Session = Depends(get_db)):
    return send_request(db, friend_in.requester_id, friend_in.addressee_id)

@router.post("/friends/accept", response_model=FriendOut)
def accept_friend(friend_in: FriendCreate, db: Session= Depends(get_db)):
    friend = accept_request(db, friend_in.requester_id, friend_in.addressee_id)
    if not friend:
        raise HTTPException(status_code=404, detail="Friend request not found or already accepted")
    return friend

@router.get("/friends", response_model=list[FriendOut])
def get_friends(user_id: int, db: Session = Depends(get_db)):
    return list_friends(db, user_id)
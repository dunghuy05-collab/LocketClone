from sqlalchemy.orm import Session
from sqlalchemy import or_
from models import friend

def send_request(db: Session, requester_id: int, addressee_id: int):
    friends = friend.FriendRequest(
        requester_id=requester_id,
        addressee_id=addressee_id,
        status='pending'
    )
    db.add(friends)
    db.commit()
    db.refresh(friends)
    return friends

def accept_request(db: Session, requester_id: int, addressee_id: int):
    friends = db.query(friend).filter(
        friend.requester_id == requester_id,
        friend.addressee_id == addressee_id,
        friend.status == 'pending',
    ).first()
    if not friends:
        return None
    friend.status = "Accepted"
    db.commit()
    db.refresh(friends)
    return friends

def list_friends(db: Session, user_id: int):
    return db.query(friend).filter(
        or_(
            (friend.requester_id == user_id),
            (friend.addressee_id == user_id),
        ),
        friend.status == 'accepted'
    ).all()


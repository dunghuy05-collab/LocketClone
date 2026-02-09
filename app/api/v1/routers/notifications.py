from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from schemas.notification import NotificationOut
from services.notification_service import list_notifications,mark_read

router = APIRouter()

@router.get("/notifications/", response_model=list[NotificationOut])
def get_notifications(user_id: int, skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return list_notifications(db, user_id, skip=skip, limit=limit)

@router.post("/notifications/{notification_id}/read", response_model=NotificationOut)
def read_notification(notification_id: int, db: Session = Depends(get_db)):
    notif = mark_read(db, notification_id)
    if not notif:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notif
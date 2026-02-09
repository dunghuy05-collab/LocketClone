from sqlalchemy.orm import Session

from models import Notification

def list_notifications(db: Session, user_id: int, skip: int = 0, limit: int= 20):
    return (
        db.query(Notification)
        .filter(Notification.user_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()

    )

def mark_read(db: Session, notification_id:int):
    notif = db.query(Notification). filter(Notification.id == notification_id).first()
    if not notif:
        return None
    notif.is_read = True
    db.commit()
    db.refresh(notif)
    return notif
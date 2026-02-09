from pydantic import BaseModel

class NotificationBase(BaseModel):
    user_id: int
    type: str
    data: dict | None = None
    is_read: bool = False

class NotificationCreate(NotificationBase):
    pass

class NotificationOut(NotificationBase):
    id: int

    class Config:
        from_attributes = True
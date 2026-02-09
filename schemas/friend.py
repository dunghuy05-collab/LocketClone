from pydantic import BaseModel

class FriendBase(BaseModel):
    requester_id: int
    addressee_id: int
    status: str = "pending"

class FriendCreate(FriendBase):
    pass

class FriendOut(FriendBase):
    id: int

    class Config:
        from_attributes = True

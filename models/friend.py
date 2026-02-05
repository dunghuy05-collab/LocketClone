from pydantic import BaseModel

class FriendBase(BaseModel):
    requester_id: int
    addressess_id: int
    status: str = 'pending'

class FriendCreate(FriendBase):
    pass

class Friendout(FriendBase):
    id: int

    class Config:
        from_attributes = True
from pydantic import BaseModel

class PhotoBase(BaseModel):
    image_url: str
    caption: str | None = None

class PhotoCreate(PhotoBase):
    user_id: int

class PhotoOut(PhotoBase):
    id: int
    user_id: int

    class Config:
        from_attribute = True
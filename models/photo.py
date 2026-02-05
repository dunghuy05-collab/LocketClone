from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.sql import func

from app.core.database import Base

class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    image_url = Column(String(500), nullable=False)
    caption = Column(String(255), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now)
    
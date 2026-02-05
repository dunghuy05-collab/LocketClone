from sqlalchemy import Column, Integer, String,Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func

from app.core.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(String(50), nullable=False)
    data = Column(JSON, nullable=True)
    is_read = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
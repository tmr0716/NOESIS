from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from datetime import datetime
from app.database import Base

class UrgentRequest(Base):
    __tablename__ = "urgent_requests"

    id = Column(Integer, primary_key=True, index=True)
    source_type = Column(String, default="Call")
    source_id = Column(Integer, nullable=True)
    description = Column(Text, nullable=False)
    severity = Column(String, default="High")
    resolved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

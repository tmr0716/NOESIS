from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"), nullable=True)
    channel = Column(String, default="WhatsApp") # WhatsApp, Instagram, SMS
    sender_type = Column(String, default="customer") # customer, ai, human
    content = Column(Text, nullable=False)
    status = Column(String, default="replied") # unanswered, replied, pending
    created_at = Column(DateTime, default=datetime.utcnow)

    contact = relationship("Contact", back_populates="messages")

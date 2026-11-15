from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base

class BusinessSettings(Base):
    __tablename__ = "business_settings"

    id = Column(Integer, primary_key=True, index=True)
    business_name = Column(String, default="NOESIS AI Receptionist")
    description = Column(Text, default="Intelligent 24/7 virtual receptionist for businesses.")
    working_hours = Column(String, default="Mon-Fri: 9:00 AM - 6:00 PM")
    contact_phone = Column(String, default="+1 (555) 019-2834")
    contact_email = Column(String, default="support@noesisai.com")
    welcome_message = Column(String, default="Hello! Thank you for calling NOESIS. How can I assist you today?")
    ai_personality = Column(String, default="Professional, warm, and helpful assistant.")
    voice_name = Column(String, default="en-US-Neural2-F")
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

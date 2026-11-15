from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"), nullable=False)
    appointment_time = Column(DateTime, nullable=False)
    status = Column(String, default="confirmed") # confirmed, rescheduled, cancelled
    service_type = Column(String, default="Consultation")
    created_at = Column(DateTime, default=datetime.utcnow)

    contact = relationship("Contact", back_populates="appointments")

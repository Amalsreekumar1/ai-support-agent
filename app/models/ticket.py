# Defines what a ticket looks like
from datetime import datetime
import enum

from sqlalchemy import Column, Integer, String, DateTime, Enum
from app.database import Base


class TicketPriority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent"


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    subject = Column(String(250))
    description = Column(String(500))
    status = Column(String(10), default = "open")
    priority = Column(String(10))
    created = Column(DateTime, default = datetime.utcnow)
    updated = Column(DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)



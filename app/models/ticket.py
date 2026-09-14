# Defines what a ticket looks like
from app.database import Base

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    subject = Column(String(250))
    description = Column(String(500))
    status = Column(String(10))
    priority = Column(String(10))
    created = Column(DateTime)
    updated = Column(DateTime)



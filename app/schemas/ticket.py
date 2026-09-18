#
from pydantic import BaseModel
from app.models.ticket import TicketPriority

class TicketCreate(BaseModel):
    subject : str
    description : str
    priority : TicketPriority = TicketPriority.medium
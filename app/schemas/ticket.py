#
class TicketCreate(BaseModel):
    subject : str
    description : str
    priority : TicketPriority = TicketPriority.medium
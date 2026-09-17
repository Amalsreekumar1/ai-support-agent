# Decides what to do with a ticket
from app.database import SessionLocal
from app.models.ticket import Ticket


def create_ticket(customer_id, ticket: TicketCreate, db):
    new_ticket = Ticket(
        customer_id = customer_id,
        subject = ticket.subject,
        description = ticket.description,
        priority = ticket.priority
    )
    db.add(new_ticket)
    db.commit()
    return new_ticket

def get_customer_tickets(customer_id, db):
    return db.query(Ticket).filter(Ticket.customer_id == customer_id).all()

def update_ticket():
    return 

def check_ticket():
    return 


# Decides what to do with a ticket
from app.database import SessionLocal
from app.models.ticket import Ticket


def create_ticket(customer_id, db):
    db.add(Ticket)
    db.commit

def get_ticket(customer_id, db):
    return db.query(Ticket).filter(Ticket.customer_id == customer_id).all()

def update_ticket():
    return 

def check_ticket():
    return 

def find_status():
    return 

def change_status():
    return 
from sqlalchemy.orm import Session

from app.models.customer import Customer

def create_customer(db: Session, customer: Customer):

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer

def get_customer_by_id(db: Session, customer_id: int):

    return (db.query(Customer).filter(Customer.id == customer_id).first())

def get_customer_by_user_id(db: Session, user_id: int):

    return (db.query(Customer).filter(Customer.user_id == user_id).first())


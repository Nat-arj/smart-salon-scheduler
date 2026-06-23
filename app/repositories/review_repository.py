from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.review import Review

def create_review(db: Session, review: Review):

    db.add(review)
    db.commit()
    db.refresh(review)

    return review

def get_review_by_id(db: Session, review_id: int):

    return (
        db.query(Review)
        .filter(Review.id == review_id)
        .first()
    )

def get_reviews_by_practitioner(db: Session, practitioner_id: int):

    return (
        db.query(Review)
        .filter(Review.practitioner_id == practitioner_id)
        .all()
    )

def get_average_rating(db: Session, practitioner_id: int):

    return (
        db.query(func.avg(Review.rating))
        .filter(Review.practitioner_id == practitioner_id)
        .scalar()
    )

def get_reviews_by_customer(db: Session, customer_id: int):

    return (
        db.query(Review)
        .filter(Review.customer_id == customer_id)
        .all()
    )

def get_review_by_appointment(db: Session, appointment_id: int):

    return (
        db.query(Review)
        .filter(
            Review.appointment_id == appointment_id
        )
        .first()
    )
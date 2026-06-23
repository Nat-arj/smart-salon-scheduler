from sqlalchemy.orm import Session

from app.models.review import Review

from app.core.enums import AppointmentStatus

from app.models.appointment import Appointment

from app.repositories import (review_repository, practitioner_repository)

def create_review(db: Session, review: Review):

    review = (review_repository.create_review(db, review))

    practitioner = (
        practitioner_repository
        .get_practitioner_by_id(
            db,
            review.practitioner_id
        )
    )

    calculate_and_update_rating(db, practitioner)

    return review

def get_review_by_id(db: Session, review_id: int):

    return (review_repository.get_review_by_id(db, review_id))

def get_reviews_by_practitioner(db: Session, practitioner_id: int):

    return (review_repository.get_reviews_by_practitioner(db, practitioner_id))

def get_reviews_by_customer(db: Session, customer_id: int):

    return (review_repository.get_reviews_by_customer(db, customer_id))

def can_review(appointment: Appointment):
    
    return (appointment.appointment_status == AppointmentStatus.COMPLETED)

def can_create_review(db: Session, appointment_id: int):

    review = (review_repository.get_review_by_appointment(
            db,
            appointment_id
        )
    )

    return review is None

def calculate_and_update_rating(db: Session, practitioner):

    reviews = (
        review_repository
        .get_reviews_by_practitioner(
            db,
            practitioner.id
        )
    )

    review_count = len(reviews)

    if review_count == 0:
        average_rating = 0

    else:
        total_rating = sum(
            review.rating
            for review in reviews
        )

        average_rating = (total_rating / review_count)

    return (
        practitioner_repository
        .update_practitioner_rating(
            db,
            practitioner,
            average_rating,
            review_count
        )
    )
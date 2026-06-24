from sqlalchemy.orm import Session

from app.models.practitioner import Practitioner

def get_practitioner_by_id(db: Session, practitioner_id:int):

    return (
        db.query(Practitioner)
        .filter(Practitioner.id==practitioner_id)
        .first()
    )

def get_practitioner_by_user_id(db: Session, user_id: int):

    return (
        db.query(Practitioner)
        .filter(
            Practitioner.user_id == user_id
        )
        .first()
    )

def get_practitioners_by_salon(db:Session, salon_id:int):

    return (
        db.query(Practitioner)
        .filter(Practitioner.salon_id==salon_id)
        .all()
    )

def update_practitioner_rating(
    db: Session,
    practitioner: Practitioner,
    rating: float,
    review_count: int
):

    practitioner.rating = rating
    practitioner.review_count = review_count
    db.commit()
    db.refresh(practitioner)

    return practitioner

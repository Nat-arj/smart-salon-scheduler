from sqlalchemy.orm import Session

from app.models.practitioner import Practitioner

def get_practitioner_by_id(db: Session, practitioner_id:int):

    return (
        db.query(Practitioner)
        .filter(Practitioner.id==practitioner_id)
        .first()
    )

def get_practitioners_by_salon(db:Session, salon_id:int):

    return (
        db.query(Practitioner)
        .filter(Practitioner.salon_id==salon_id)
        .all()
    )


from datetime import date

from sqlalchemy.orm import Session

from app.models.practitioner_unavailability import PractitionerUnavailability

def get_unavailability_by_date(db: Session, practitioner_id: int, slot_date: date):

    return (
        db.query(PractitionerUnavailability)
        .filter(
            PractitionerUnavailability.practitioner_id == practitioner_id,
            PractitionerUnavailability.start_date <= slot_date,
            PractitionerUnavailability.end_date >= slot_date
        )
        .all()
    )

def create_unavailability(db: Session, unavailability: PractitionerUnavailability):

    db.add(unavailability)
    db.commit()
    db.refresh(unavailability)

    return unavailability

def remove_unavailability(db: Session, unavailability: PractitionerUnavailability):

    db.delete(unavailability)
    db.commit()

def get_current_unavailability(db: Session, practitioner_id: int):

    return (
        db.query(PractitionerUnavailability)
        .filter(PractitionerUnavailability.practitioner_id == practitioner_id)
        .all()
    )
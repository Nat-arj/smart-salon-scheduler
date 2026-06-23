from sqlalchemy.orm import Session

from app.models.practitioner_service import PractitionerService

def get_practitioner_services(db: Session, practitioner_id: int):

    return (
        db.query(PractitionerService)
        .filter(PractitionerService.practitioner_id == practitioner_id)
        .all()
    )

def has_service(db: Session, practitioner_id: int, service_id: int):

    return (
        db.query(PractitionerService)
        .filter(
            PractitionerService.practitioner_id == practitioner_id,
            PractitionerService.service_id == service_id
        )
        .first()
    )

def assign_service(db: Session, practitioner_service: PractitionerService):

    db.add(practitioner_service)
    db.commit()
    db.refresh(practitioner_service)

    return practitioner_service

def remove_service(db: Session, practitioner_service: PractitionerService):
    
    db.delete(practitioner_service)
    db.commit()


from datetime import date

from sqlalchemy.orm import Session

from app.repositories import (
    availability_repository,
    practitioner_unavailability_repository
)

from app.core.enums import SlotStatus

def get_available_slots(db: Session, practitioner_id: int, slot_date: date):

    return (
        availability_repository
        .get_available_slots(
            db,
            practitioner_id,
            slot_date
        )
    )

def hold_slots(db: Session, slots: list):

    for slot in slots:
        availability_repository.hold_slot(db, slot)

    return slots

def release_slots(db: Session, slots: list):

    for slot in slots:
        availability_repository.release_slot(db, slot)

    return slots

def block_unavailability(db: Session, practitioner_id: int, slot_date: date):

    unavailable_periods = (
        practitioner_unavailability_repository
        .get_unavailability_by_date(
            db,
            practitioner_id,
            slot_date
        )
    )

    if unavailable_periods:
        slots = (
            availability_repository
            .get_available_slots(
                db,
                practitioner_id,
                slot_date
             )
        )
    
    for slot in slots:
            availability_repository.update_slot_status(
                db,
                slot,
                SlotStatus.UNAVAILABLE
            )
                


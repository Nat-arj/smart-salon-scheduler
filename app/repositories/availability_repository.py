from datetime import date, time, datetime, timedelta, timezone

from sqlalchemy.orm import Session

from app.models.availability_slot import AvailabilitySlot

from app.core.enums import SlotStatus

from app.core.config import settings

def get_available_slots(db: Session, practitioner_id: int, slot_date: date):

    return (
        db.query(AvailabilitySlot)
        .filter(
            AvailabilitySlot.practitioner_id == practitioner_id,
            AvailabilitySlot.slot_date == slot_date,
            AvailabilitySlot.status == SlotStatus.AVAILABLE
        )
        .all()
    )

def get_slot(db: Session, practitioner_id: int, slot_date: date, start_time: time):

    return (
        db.query(AvailabilitySlot)
        .filter(
            AvailabilitySlot.practitioner_id == practitioner_id,
            AvailabilitySlot.slot_date == slot_date,
            AvailabilitySlot.start_time == start_time
        )
        .first()
    )

def hold_slot(db: Session, slot: AvailabilitySlot):

    slot.status=SlotStatus.HELD
    db.commit()
    db.refresh(slot)

    return slot

def book_slot(db: Session, slot: AvailabilitySlot):

    slot.status=SlotStatus.BOOKED
    db.commit()
    db.refresh(slot)

    return slot

def release_slot(db: Session, slot: AvailabilitySlot):

    slot.status=SlotStatus.AVAILABLE
    db.commit()
    db.refresh(slot)

    return slot

def block_slots(db: Session, slots: list[AvailabilitySlot]):
    
    for slot in slots:
        slot.status=SlotStatus.BOOKED

    db.commit()

    return slots

def release_slots(db: Session, slots: list[AvailabilitySlot]):

    for slot in slots:
        slot.status=SlotStatus.AVAILABLE

    db.commit()

    return slots

def get_consecutive_slots(
    db: Session, 
    practitioner_id: int,
    slot_date: date,
    start_time: time,
    count: int
):

    slots = (
        db.query(AvailabilitySlot)
        .filter(
            AvailabilitySlot.practitioner_id == practitioner_id,
            AvailabilitySlot.slot_date == slot_date,
            AvailabilitySlot.start_time >= start_time,
            AvailabilitySlot.status == SlotStatus.AVAILABLE
        )
        .order_by(
            AvailabilitySlot.start_time
        )
        .all()
    )

    if len(slots) < count:
        return None
    
    consecutive = [slots[0]]

    for i in range(1, len(slots)):
        previous = datetime.combine(slot_date,consecutive[-1].start_time)
        current = datetime.combine(slot_date, slots[i].start_time)

        if current - previous == timedelta(minutes=settings.SLOT_DURATION):
            consecutive.append(slots[i])

            if len(consecutive) == count:
                return consecutive

        else:
            consecutive = [slots[i]]
        
    return None

def update_slot_status(db: Session, slot: AvailabilitySlot, status: SlotStatus):

    slot.status = status

    db.commit()
    db.refresh(slot)

    return slot

def get_expired_held_slots(db: Session):

    now = datetime.now(timezone.utc)

    return (
        db.query(AvailabilitySlot)
        .filter(
            AvailabilitySlot.status == SlotStatus.HELD,
            AvailabilitySlot.hold_until <= now
        )
        .all()
    )
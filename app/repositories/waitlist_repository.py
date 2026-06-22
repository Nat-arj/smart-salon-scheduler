from datetime import date, time

from sqlalchemy.orm import Session

from app.models.waitlist import Waitlist

def join_waitlist(db: Session, waitlist: Waitlist):

    db.add(waitlist)
    db.commit()
    db.refresh(waitlist)

    return waitlist

def get_waitlist_by_practitioner(db: Session, practitioner_id: int):

    return (
        db.query(Waitlist)
        .filter(Waitlist.practitioner_id == practitioner_id)
        .all()
    )

def get_waitlist_by_slot(
    db: Session,
    practitioner_id: int,
    preferred_date: date,
    preferred_time: time
):

    return (
        db.query(Waitlist)
        .filter(
            Waitlist.practitioner_id == practitioner_id,
            Waitlist.preferred_date == preferred_date,
            Waitlist.preferred_time == preferred_time
        )
        .all()
    )

def mark_as_notified(db: Session, waitlist: Waitlist):
    
    waitlist.notified = True
    db.commit()
    db.refresh(waitlist)

    return waitlist

def remove_from_waitlist(db: Session, waitlist: Waitlist):

    db.delete(waitlist)
    db.commit()
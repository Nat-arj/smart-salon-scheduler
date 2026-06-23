from sqlalchemy.orm import Session

from datetime import date, time

from app.models.waitlist import Waitlist

from app.repositories import waitlist_repository


def join_waitlist(db: Session, waitlist: Waitlist):

    return (
        waitlist_repository
        .join_waitlist(
            db,
            waitlist
        )
    )

def get_waitlist_by_slot(
    db: Session,
    practitioner_id: int,
    preferred_date: date,
    preferred_time: time
):

    return (
        waitlist_repository
        .get_waitlist_by_slot(
            db,
            practitioner_id,
            preferred_date,
            preferred_time
        )
    )

def notify_waitlist(waitlist: Waitlist):

    print(f"Notify customer {waitlist.customer_id}")

def remove_from_waitlist(db: Session, waitlist: Waitlist):

    waitlist_repository.remove_from_waitlist(db, waitlist)


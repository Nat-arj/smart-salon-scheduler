from datetime import date

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.availability_schema import AvailabilityResponse

from app.services import availability_service

from app.auth.dependencies import get_current_user

from app.models.user import User

router = APIRouter(prefix="/availability", tags=["Availability"])

@router.get("/{practitioner_id}", response_model=list[AvailabilityResponse])
def get_available_slots(
    practitioner_id: int,
    slot_date: date,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return (
        availability_service
        .get_available_slots(
            db,
            practitioner_id,
            slot_date
        )
    )
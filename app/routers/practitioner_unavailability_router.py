from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.auth.dependencies import get_current_practitioner

from app.models.user import User

from app.models.practitioner_unavailability import PractitionerUnavailability

from app.repositories import (
    practitioner_repository,
    practitioner_unavailability_repository
)

from app.schemas.unavailability_schema import (
    PractitionerUnavailabilityCreate,
    PractitionerUnavailabilityResponse
)

router = APIRouter(
    prefix="/unavailability",
    tags=["Practitioner Unavailability"]
)

@router.post("/",response_model=PractitionerUnavailabilityResponse)
def create_unavailability(
    data: PractitionerUnavailabilityCreate,
    current_user: User = Depends(get_current_practitioner),
    db: Session = Depends(get_db)
):
    
    practitioner = (
    practitioner_repository
    .get_practitioner_by_user_id(
        db,
        current_user.id
    )
)
    
    if practitioner is None:
        raise HTTPException(
            status_code=404,
            detail="Practitioner not found"
        )
    
    unavailability = PractitionerUnavailability(
    practitioner_id=practitioner.id,
    start_date=data.start_date,
    end_date=data.end_date,
    leave_type=data.leave_type,
    reason=data.reason
)
    
    return (
    practitioner_unavailability_repository
    .create_unavailability(
        db,
        unavailability
    )
)

@router.get("/", response_model=list[PractitionerUnavailabilityResponse])
def get_unavailability(
    current_user: User = Depends(get_current_practitioner),
    db: Session = Depends(get_db)
):
    
    practitioner = (
    practitioner_repository
    .get_practitioner_by_user_id(
        db,
        current_user.id
    )
)
    
    return (
    practitioner_unavailability_repository
    .get_current_unavailability(
        db,
        practitioner.id
    )
)

@router.delete("/{unavailability_id}")
def delete_unavailability(
    unavailability_id: int,
    current_user: User = Depends(get_current_practitioner),
    db: Session = Depends(get_db)
):
    
    leave = (
    practitioner_unavailability_repository
    .get_unavailability_by_id(
        db,
        unavailability_id
    )
)
    
    if leave is None:
        raise HTTPException(
            status_code=404,
            detail="Record not found"
        )
    
    practitioner = (
        practitioner_repository
        .get_practitioner_by_user_id(
            db,
            current_user.id
        )
    )

    if leave.practitioner_id != practitioner.id:
        raise HTTPException(
            status_code=403,
            detail="Access Denied"
        )

    practitioner_unavailability_repository.remove_unavailability(db, leave)

    return {"message": "Unavailability deleted successfully"}


        

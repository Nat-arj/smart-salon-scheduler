from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.review_schema import (ReviewCreate, ReviewResponse)

from app.services import review_service

from app.auth.dependencies import get_current_user

from app.repositories import (customer_repository, appointment_repository)

from app.models.user import User

from app.models.review import Review

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.post("/", response_model=ReviewResponse)
def create_review(
    review_data: ReviewCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    
    customer = (
    customer_repository
    .get_customer_by_user_id(
        db,
        current_user.id
    )
)
    
    appointment = (
    appointment_repository
    .get_appointment_by_id(
        db,
        review_data.appointment_id
    )
)
    
    if not review_service.can_review(appointment):
        raise HTTPException(
            status_code=400,
            detail="Appointment not completed"
        )
    
    if not review_service.can_create_review(
        db,
        review_data.appointment_id
    ):
        raise HTTPException(
            status_code=400,
            detail="Review already exists"
        )

    review = Review(
    customer_id=customer.id,
    appointment_id=review_data.appointment_id,
    practitioner_id=review_data.practitioner_id,
    rating=review_data.rating,
    review_text=review_data.review_text
)
    
    return (
    review_service
    .create_review(
        db,
        review
    )
)

@router.get(
    "/practitioner/{practitioner_id}",
    response_model=list[ReviewResponse]
)
def get_reviews_by_practitioner(
    practitioner_id: int,
    db: Session = Depends(get_db)
):

    return (
        review_service
        .get_reviews_by_practitioner(
            db,
            practitioner_id
        )
    )

@router.get("/{review_id}", response_model=ReviewResponse)
def get_review(
    review_id: int,
    db: Session = Depends(get_db)
):

    review = (
        review_service
        .get_review_by_id(
            db,
            review_id
        )
    )

    if review is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found"
        )

    return review
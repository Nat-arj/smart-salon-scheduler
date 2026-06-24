from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.user import User

from app.services import payment_service

from app.repositories import (
    payment_repository, 
    customer_repository, 
    appointment_repository,
    practitioner_repository
)

from app.auth.dependencies import (
    get_current_customer, 
    get_current_admin,
    get_current_practitioner    
)
    
router = APIRouter(prefix="/payments", tags=["Payments"])

@router.get("/my/{appointment_id}")
def get_payments_by_appointment(
    appointment_id: int, 
    current_user: User = Depends(get_current_customer),
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
        appointment_id
    )
)
    
    if appointment.customer_id != customer.id:
        raise HTTPException(
            status_code=403,
            detail="Access Denied"
        )

    return (
        payment_repository
        .get_payments_by_appointment(
            db,
            appointment_id
        )
    )

@router.get("/practitioner")

def get_practitioner_payments(
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

    return (
        payment_repository
        .get_payments_by_practitioner(
            db,
            practitioner.id
        )
    )


@router.patch("/{payment_id}/success")
def mark_payment_success(
    payment_id: int,
    current_user: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):

    payment = (
        payment_repository
        .get_payment_by_id(
            db,
            payment_id
        )
    )

    if payment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payment not found"
        )

    return (
        payment_service
        .mark_payment_success(
            db,
            payment
        )
    )

@router.patch("/{payment_id}/failed")
def mark_payment_failed(
    payment_id: int,
    current_user: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):

    payment = (
        payment_repository
        .get_payment_by_id(
            db,
            payment_id
        )
    )

    if payment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payment not found"
        )

    return (
        payment_service
        .mark_payment_failed(
            db,
            payment
        )
    )

@router.patch("/{payment_id}/refund")
def refund_payment(
    payment_id: int,
    current_user: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):

    payment = (
        payment_repository
        .get_payment_by_id(
            db,
            payment_id
        )
    )

    if payment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payment not found"
        )

    return (
        payment_service
        .refund_payment(
            db,
            payment
        )
    )

@router.post("/remaining/{appointment_id}")
def create_remaining_payment(
    appointment_id:int,
    current_user: User = Depends(get_current_customer),
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
        appointment_id
    )
)
    
    if appointment.customer_id != customer.id:
        raise HTTPException(
            status_code=403,
            detail="Access Denied"
        )

    return (
        payment_service
        .create_remaining_payment(
            db,
            appointment_id
        )
    )
from datetime import date

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.appointment_schema import (
    AppointmentCreate,
    AppointmentResponse
)

from app.core.enums import UserRole

from app.services import appointment_service

from app.auth.dependencies import (
    get_current_customer, 
    get_current_practitioner,
    get_current_user
)
from app.models.user import User

from app.repositories import customer_repository, practitioner_repository

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/", response_model=AppointmentResponse)
def create_appointment(
    appointment_data: AppointmentCreate,
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

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    
    customer_id = customer.id

    return appointment_service.book_appointment(
        db,
        customer_id,
        appointment_data.practitioner_id,
        appointment_data.service_id,
        appointment_data.appointment_date,
        appointment_data.start_time
    )

@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(
    appointment_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    appointment = (appointment_service.get_appointment_by_id(db, appointment_id))

    if appointment is None:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )
    
    if current_user.role == UserRole.CUSTOMER:
        customer = (
            customer_repository
            .get_customer_by_user_id(
                db,
                current_user.id
            )
        )

        if appointment.customer_id != customer.id:
            raise HTTPException(
                status_code=403,
                detail="Access Denied"
            )
    
    elif current_user.role == UserRole.PRACTITIONER:
        practitioner = (
            practitioner_repository
            .get_practitioner_by_user_id(
                db,
                current_user.id
            )
        )

        if appointment.practitioner_id != practitioner.id:
            raise HTTPException(
                status_code=403,
                detail="Access Denied"
            )
    
    elif current_user.role == UserRole.ADMIN:
        pass

    return appointment

@router.get("/my")
def get_customer_appointments(
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
    
    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return (
        appointment_service
        .get_customer_appointments(
            db,
            customer.id
        )
    )

@router.get("/practitioner")
def get_practitioner_appointments(
    appointment_date: date,
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
        appointment_service
        .get_practitioner_appointments(
            db,
            practitioner.id,
            appointment_date
        )
    )

@router.patch("/{appointment_id}/complete")
def complete_appointment(
    appointment_id: int,
    current_user: User = Depends(get_current_practitioner),
    db: Session = Depends(get_db)
):

    return (
        appointment_service
        .complete_appointment(
            db,
            appointment_id
        )
    )
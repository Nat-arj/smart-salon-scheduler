from datetime import date
from datetime import time

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.appointment import Appointment
from app.models.payment import Payment

from app.core.config import settings

from app.core.enums import (
    AppointmentStatus,
    PaymentStatus,
    PaymentType
)

from app.repositories import (
    appointment_repository,
    availability_repository,
    payment_repository,
    practitioner_repository,
    service_repository
)

def book_appointment(
    db: Session,
    customer_id: int,
    practitioner_id: int,
    service_id: int,
    appointment_date: date,
    start_time: time
):
    
    practitioner = (
    practitioner_repository
    .get_practitioner_by_id(
        db,
        practitioner_id
    )
)

    if not practitioner:
        raise HTTPException(status_code=404, detail="Practitioner not found")
    
    service = (
    service_repository
    .get_service_by_id(
        db,
        service_id
    )
)

    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    
    required_slots = (service.duration_minutes // settings.SLOT_DURATION)

    slots = (
    availability_repository
    .get_consecutive_slots(
        db,
        practitioner_id,
        appointment_date,
        start_time,
        required_slots
    )
)
    
    if not slots:
        raise HTTPException(
        status_code=400,
        detail="Required consecutive slots unavailable"
    )

    for slot in slots:
        availability_repository.hold_slot(db, slot)

    appointment = Appointment(
    customer_id=customer_id,
    practitioner_id=practitioner_id,
    service_id=service_id,
    appointment_date=appointment_date,
    start_time=start_time,
    end_time=slots[-1].end_time,
    status=AppointmentStatus.HELD
)
    
    deposit_amount = int(service.base_price * settings.DEPOSIT_PERCENTAGE)

    appointment = (appointment_repository.create_appointment(db, appointment))

    payment = Payment(
    appointment_id=appointment.id,
    customer_id=customer_id,
    amount=deposit_amount,
    payment_type=PaymentType.DEPOSIT,
    status=PaymentStatus.PENDING
)
    
    payment_repository.create_payment(db, payment)

    return {
    "message": "Appointment held successfully",
    "appointment_id": appointment.id,
    "payment_status": PaymentStatus.PENDING
}
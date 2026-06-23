from datetime import date, time

from sqlalchemy.orm import Session

from app.models.appointment import Appointment

from app.core.enums import AppointmentStatus

def create_appointment(db: Session, appointment: Appointment):

    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    return appointment

def get_appointment_by_id(db: Session, appointment_id: int):

    return (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )

def get_customer_appointments(db: Session, customer_id: int):

    return (
        db.query(Appointment)
        .filter(Appointment.customer_id == customer_id)
        .all()
    )

def get_practitioner_appointments(
    db: Session,
    practitioner_id: int,
    appointment_date: date
):
    
    return (
        db.query(Appointment)
        .filter(
            Appointment.practitioner_id == practitioner_id,
            Appointment.appointment_date == appointment_date
        )
        .all()
    )

def get_customer_appointments_by_status(
    db: Session,
    customer_id: int,
    status: AppointmentStatus
):

    return (
        db.query(Appointment)
        .filter(
            Appointment.customer_id == customer_id,
            Appointment.appointment_status == status
        )
        .all()
    )

def update_appointment_status(
    db: Session,
    appointment: Appointment,
    status: AppointmentStatus
):

    appointment.appointment_status = status
    db.commit()
    db.refresh(appointment)

    return appointment


def reschedule_appointment(
    db: Session,
    appointment: Appointment,
    appointment_date: date,
    start_time: time,
    end_time: time
):

    appointment.appointment_date = (appointment_date)
    appointment.start_time = start_time
    appointment.end_time = end_time
    appointment.appointment_status = (AppointmentStatus.RESCHEDULED)
    db.commit()
    db.refresh(appointment)

    return appointment
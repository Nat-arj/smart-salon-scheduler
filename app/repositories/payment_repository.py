from sqlalchemy.orm import Session

from app.models.payment import Payment

from app.models.appointment import Appointment

from app.core.enums import PaymentStatus

def create_payment(db: Session, payment: Payment):

    db.add(payment)
    db.commit()
    db.refresh(payment)

    return payment

def get_payment_by_id(db: Session, payment_id: int):

    return (
        db.query(Payment)
        .filter(Payment.id == payment_id)
        .first()
    )

def get_payments_by_appointment(db: Session, appointment_id: int):

    return (
        db.query(Payment)
        .filter(Payment.appointment_id == appointment_id)
        .all()
    )

def update_payment_status(
    db: Session,
    payment: Payment,
    status: PaymentStatus
):

    payment.payment_status = status
    db.commit()
    db.refresh(payment)

    return payment

def get_payments_by_customer(db: Session, customer_id: int):

     return (
        db.query(Payment)
        .join(Appointment)
        .filter(
            Appointment.customer_id
            == customer_id
        )
        .all()
    )

def get_payments_by_status(db: Session, status: PaymentStatus):

    return (
        db.query(Payment)
        .filter(Payment.payment_status == status)
        .all()
    )

def get_payments_by_practitioner(db: Session, practitioner_id: int):

    return (
        db.query(Payment)
        .join(
            Appointment,
            Payment.appointment_id == Appointment.id
        )
        .filter(
            Appointment.practitioner_id == practitioner_id
        )
        .all()
    )



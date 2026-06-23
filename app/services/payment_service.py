from sqlalchemy.orm import Session

from app.models.payment import Payment

from app.core.config import DEPOSIT_PERCENTAGE

from app.core.enums import (
    PaymentStatus,
    PaymentType
)

from app.repositories import payment_repository


def calculate_initial_payment(service_price: float):

    if service_price < 1000:
        return {"amount": service_price, "payment_type": PaymentType.FULL}

    deposit_amount = (service_price * DEPOSIT_PERCENTAGE)

    return {"amount": deposit_amount, "payment_type": PaymentType.DEPOSIT}

def calculate_remaining_amount(total_amount: float, deposit_amount: float):

    return total_amount - deposit_amount

def create_payment(db: Session, payment: Payment):

    return payment_repository.create_payment(db, payment)

def mark_payment_success(db: Session, payment: Payment):

    return payment_repository.update_payment_status(
        db,
        payment,
        PaymentStatus.SUCCESS
    )

def mark_payment_failed(db: Session, payment: Payment):

    return payment_repository.update_payment_status(
        db,
        payment,
        PaymentStatus.FAILED
    )

def refund_payment(db: Session, payment: Payment):

    return payment_repository.update_payment_status(
        db,
        payment,
        PaymentStatus.REFUNDED
    )

def calculate_no_show_fee(amount: float):

    return amount * 0.50

def is_fully_paid(db: Session, appointment_id: int, total_price: float):

    payments = (
        payment_repository
        .get_payments_by_appointment(
            db,
            appointment_id
        )
    )

    paid_amount = sum(
        payment.amount
        for payment in payments
        if payment.payment_status == PaymentStatus.SUCCESS
    )

    return paid_amount >= total_price
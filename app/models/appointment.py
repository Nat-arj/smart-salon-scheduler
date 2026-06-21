from sqlalchemy import Column, Integer, Date, Time, DateTime, ForeignKey, Enum, String

from sqlalchemy.orm import relationship

from datetime import datetime
from datetime import timezone

from app.db.database import Base

from app.core.enums import (AppointmentStatus, PaymentStatus)

class Appointment(Base):

    __tablename__="appointments"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)

    practitioner_id = Column(
        Integer,
        ForeignKey("practitioners.id"),
        nullable=False
    )

    service_id = Column(
        Integer,
        ForeignKey("services.id"),
        nullable=False
    )

    appointment_date = Column(Date, nullable=False)

    start_time = Column(Time, nullable=False)

    end_time = Column(Time, nullable=False)

    appointment_status = Column(
        Enum(AppointmentStatus),
        nullable=False,
        default=AppointmentStatus.BOOKED
    )

    payment_status = Column(
        Enum(PaymentStatus),
        nullable=False,
        default=PaymentStatus.PENDING
    )

    cancellation_reason = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    customer = relationship("Customer")

    practitioner = relationship("Practitioner")

    service = relationship("Service")
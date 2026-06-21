from sqlalchemy import Column, Integer, Float, String, ForeignKey, Enum, DateTime

from sqlalchemy.orm import relationship

from datetime import datetime
from datetime import timezone

from app.db.database import Base

from app.core.enums import (PaymentStatus, PaymentType)

class Payment(Base):

    __tablename__="payments"

    id = Column(Integer, primary_key=True, index=True)

    appointment_id = Column(
        Integer,
        ForeignKey("appointments.id"),
        nullable=False
    )

    payment_type = Column(Enum(PaymentType), nullable=False)

    amount = Column(Float, nullable=False)

    payment_status = Column(
        Enum(PaymentStatus),
        nullable=False,
        default=PaymentStatus.PENDING
    )

    transaction_id = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    appointment = relationship("Appointment")
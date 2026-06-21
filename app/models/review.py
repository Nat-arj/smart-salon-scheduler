from sqlalchemy import Column, Integer, ForeignKey, Float, Text, DateTime

from sqlalchemy.orm import relationship

from datetime import datetime
from datetime import timezone

from app.db.database import Base

class Review(Base):

    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False
    )

    practitioner_id = Column(
        Integer,
        ForeignKey("practitioners.id"),
        nullable=False
    )

    appointment_id = Column(
        Integer,
        ForeignKey("appointments.id"),
        nullable=False
    )

    rating = Column(Float, nullable=False)

    review_text = Column(Text, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    customer = relationship("Customer")

    practitioner = relationship("Practitioner")

    appointment = relationship("Appointment")
from sqlalchemy import Column, Integer, Date, Time, DateTime, ForeignKey, Boolean

from sqlalchemy.orm import relationship

from datetime import datetime
from datetime import timezone

from app.db.database import Base

class Waitlist(Base):

    __tablename__ = "waitlist"


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

    preferred_date = Column(Date, nullable=False)

    preferred_time = Column(Time, nullable=False)

    notified = Column(Boolean, default=False)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda:
        datetime.now(timezone.utc)
    )

    customer = relationship("Customer")

    practitioner = relationship("Practitioner")


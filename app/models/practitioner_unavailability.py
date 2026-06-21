from sqlalchemy import Column, Integer, Date, Enum, ForeignKey, String, DateTime
from datetime import datetime
from datetime import timezone

from app.core.enums import LeaveType

from sqlalchemy.orm import relationship

from app.db.database import Base

class PractitionerUnavailability(Base):

    __tablename__="practitioner_unavailability"

    id = Column(Integer, primary_key=True, index=True)

    practitioner_id = Column(
        Integer,
        ForeignKey("practitioners.id"),
        nullable=False
    )

    start_date = Column(Date, nullable=False)

    end_date = Column(Date, nullable=False)

    leave_type = Column(Enum(LeaveType), nullable=False)

    reason = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    practitioner = relationship("Practitioner")
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Date
from sqlalchemy import Time
from sqlalchemy import ForeignKey
from sqlalchemy import Enum
from sqlalchemy import DateTime

from sqlalchemy.orm import relationship

from datetime import datetime
from datetime import timezone

from app.db.database import Base

from app.core.enums import SlotStatus

class AvailabilitySlot(Base):

    __tablename__="availability_slots"

    id = Column(Integer, primary_key=True, index=True)

    practitioner_id = Column(
        Integer,
        ForeignKey("practitioners.id"),
        nullable=False
    )

    slot_date = Column(Date, nullable=False)

    start_time = Column(Time, nullable=False)

    end_time = Column(Time, nullable=False)

    status = Column(
        Enum(SlotStatus),
        nullable=False,
        default=SlotStatus.AVAILABLE
    )

    hold_until = Column(DateTime(timezone=True), nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    practitioner = relationship("Practitioner")
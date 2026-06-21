from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from datetime import datetime
from datetime import timezone

from sqlalchemy.orm import relationship

from app.db.database import Base

class Customer(Base):

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    phone = Column(String)

    favorite_practitioner_id = Column(
        Integer,
        ForeignKey("practitioners.id"),
        nullable=True
    )

    preferences = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    user = relationship("User")

    favorite_practitioner = relationship("Practitioner")
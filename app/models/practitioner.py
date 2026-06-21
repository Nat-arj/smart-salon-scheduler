from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Text
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from datetime import datetime
from datetime import timezone
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.db.database import Base

class Practitioner(Base):

    __tablename__ = "practitioners"

    id = Column(Integer, primary_key=True, index=True)

    salon_id = Column(Integer, ForeignKey("salons.id"), nullable=False)

    name = Column(String, nullable=False)

    experience_years = Column(Integer, default=0)

    speciality = Column(String)

    rating = Column(Float, default=0.0)

    review_count = Column(Integer, default=0)

    photo_url = Column(Text)

    bio = Column(Text)

    is_active = Column(Boolean, default=True)

    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    salon = relationship("Salon", back_populates="practitioners")

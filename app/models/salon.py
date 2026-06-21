from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Text
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from datetime import datetime
from datetime import timezone

from app.db.database import Base

class Salon(Base):

    __tablename__ = "salons"

    id = Column(Integer, primary_key=True, index=True)

    google_place_id = Column(String, unique=True, nullable=False)

    name = Column(String, nullable=False)

    address = Column(Text, nullable=False)

    phone = Column(String)

    rating = Column(Float, default=0.0)

    review_count = Column(Integer, default=0)

    latitude = Column(Float)

    longitude = Column(Float)

    opening_hours = Column(Text)

    photo_url = Column(Text)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.db.database import Base

class PractitionerService(Base):

    __tablename__="practitioner_services"

    id = Column(Integer, primary_key=True, index=True)

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

    price = Column(Float, nullable=False)

    experience_level = Column(Integer)

    practitioner = relationship("Practitioner")

    service = relationship("Service")
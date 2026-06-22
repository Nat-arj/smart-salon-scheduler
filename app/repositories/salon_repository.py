from sqlalchemy.orm import Session

from app.models.salon import Salon

def get_all_salons(db: Session):

    return (db.query(Salon).filter(Salon.is_active == True).all())

def get_salon_by_id(db: Session, salon_id:int):

    return (db.query(Salon).filter(Salon.id == salon_id).first())


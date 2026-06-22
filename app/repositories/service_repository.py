from sqlalchemy.orm import Session

from app.models.service import Service

def create_service(db: Session, service: Service):

    db.add(service)
    db.commit()
    db.refresh(service)

    return service

def get_service_by_id(db: Session, service_id: int):

    return (db.query(Service).filter(Service.id == service_id).first())

def get_all_services(db: Session):

    return (db.query(Service).filter(Service.is_active == True).all())

def update_service(db: Session, service: Service):
    
    db.commit()
    db.refresh(service)

    return service

def deactivate_service(db: Session, service: Service):

    service.is_active=False
    db.commit()
    db.refresh(service)

    return service

def search_services(db: Session, keyword:str):

    return (db.query(Service).filter(Service.name.ilike(f"%{keyword}%")).all())
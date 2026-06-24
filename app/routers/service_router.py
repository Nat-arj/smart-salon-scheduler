from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.repositories import service_repository

from app.models.user import User

from app.models.service import Service

from app.db.database import get_db

from app.schemas.service_schema import ServiceResponse, ServiceCreate

from app.auth.dependencies import get_current_user, get_current_admin


router = APIRouter(prefix="/service", tags=["Service"])

@router.get("/", response_model=list[ServiceResponse])
def get_all_services(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return (
        service_repository
        .get_all_services(
            db
        )
    )

@router.get("/{service_id}", response_model=ServiceResponse)
def get_service(
    service_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    service = (
        service_repository
        .get_service_by_id(
            db,
            service_id
        )
    )

    if service is None:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )
    
    return service

@router.get("/search/{keyword}")
def search_services(
    keyword: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return (
        service_repository
        .search_services(
            db,
            keyword
        )
    )

@router.post("/", response_model=ServiceResponse)
def create_service(
    service_data: ServiceCreate,
    current_user: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    
    service = Service(
    name=service_data.name,
    description=service_data.description,
    duration_minutes=service_data.duration_minutes,
    base_price=service_data.base_price
)
    
    return (
    service_repository
    .create_service(
        db,
        service
    )
)

@router.patch("/{service_id}")
def update_service(
    service_id: int,
    service_data: ServiceCreate,
    current_user: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    
    service = (
    service_repository
    .get_service_by_id(
        db,
        service_id
    )
)
    
    service.name = service_data.name
    service.description = service_data.description
    service.duration_minutes = service_data.duration_minutes
    service.base_price = service_data.base_price

    return (
    service_repository
    .update_service(
        db,
        service
    )
)

@router.delete("/{service_id}")
def delete_service(
    service_id: int,
    current_user: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    
    service = (
    service_repository
    .get_service_by_id(
        db,
        service_id
    )
)
    
    return (
    service_repository
    .deactivate_service(
        db,
        service
    )
)
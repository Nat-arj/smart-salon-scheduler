from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.repositories import salon_repository

from app.auth.dependencies import (
    get_current_user,
    get_current_admin
)

from app.models.user import User

from app.schemas.salon_schema import SalonResponse

router = APIRouter(prefix="/salons", tags=["Salons"])


@router.get("/", response_model=list[SalonResponse])
def get_salons(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return (
        salon_repository
        .get_all_salons(
            db
        )
    )

@router.get("/{salon_id}", response_model=SalonResponse)
def get_salon(
    salon_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    salon = (
        salon_repository
        .get_salon_by_id(
            db,
            salon_id
        )
    )

    if salon is None:
        raise HTTPException(
            status_code=404,
            detail="Salon not found"
        )

    return salon



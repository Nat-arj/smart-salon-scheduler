from fastapi import APIRouter

from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.user_schema import (UserCreate, UserResponse)

from app.services import auth_service

from app.schemas.auth_schema import LoginRequest

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):

    return (
        auth_service
        .register_customer(
            db,
            user_data
        )
    )

@router.post("/login")
def login(login_data: LoginRequest, db: Session = Depends(get_db)):

    return (
        auth_service
        .login_user(
            db,
            login_data.email,
            login_data.password
        )
    )


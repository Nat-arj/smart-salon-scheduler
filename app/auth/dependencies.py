from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordBearer

from app.auth.jwt_handler import verify_token

from app.db.database import get_db

from app.repositories import user_repository

from app.core.enums import UserRole

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    payload = verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    user = (
        user_repository
        .get_user_by_email(
            db,
            payload["sub"]
        )
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

def get_current_admin(user=Depends(get_current_user)):

    if user["role"]!=UserRole.ADMIN:

        raise HTTPException(
            status_code=403,
            detail="Access Denied"
        )

    return user

def get_current_practitioner(user=Depends(get_current_user)):

    if user["role"]!=UserRole.PRACTITIONER:

        raise HTTPException(
            status_code=403,
            detail="Access Denied"
        )

    return user

def get_current_customer(user = Depends(get_current_user)):

    if user["role"] != UserRole.CUSTOMER:
        raise HTTPException(
            status_code=403,
            detail="Only customers allowed"
        )
    return user
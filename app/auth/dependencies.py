from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import OAuth2PasswordBearer

from app.auth.jwt_handler import verify_token

from app.core.enums import UserRole

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token:str=Depends(oauth2_scheme)):

    payload=verify_token(token)

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return payload

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
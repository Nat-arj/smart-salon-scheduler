from sqlalchemy.orm import Session

from fastapi import HTTPException

from fastapi import status

from app.models.user import User

from app.models.customer import Customer

from app.schemas.user_schema import UserCreate

from app.core.enums import UserRole

from app.auth.hash import hash_password, verify_password

from app.auth.jwt_handler import create_access_token

from app.repositories import (
    user_repository,
    customer_repository
)

def register_customer(db: Session, user_data: UserCreate):

    existing_user = (
        user_repository
        .get_user_by_email(
            db,
            user_data.email
        )
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    hashed_password = (hash_password(user_data.password))

    user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash=hashed_password,
        role=UserRole.CUSTOMER
    )

    user = (user_repository.create_user(db, user))

    customer = Customer(
        user_id=user.id,
        phone=user_data.phone
    )

    customer_repository.create_customer(db, customer)

    return user

def authenticate_user(db: Session, email: str, password: str):

    user = (user_repository.get_user_by_email(db, email))

    if not user.is_active:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user

def login_user(db: Session, email: str, password: str):

    user = authenticate_user(db, email, password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = (create_access_token({"sub": user.email, "role": user.role}))

    return {"access_token": token, "token_type": "bearer"}

def change_password(db: Session, user: User, new_password: str):

    hashed_password = (hash_password(new_password))

    user.password_hash = hashed_password

    return (user_repository.update_user(db, user))

def deactivate_user(db: Session, user: User):

    user.is_active = False

    return (user_repository.update_user(db, user))

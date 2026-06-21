from pydantic import BaseModel
from pydantic import EmailStr

from app.core.enums import UserRole

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):

    name: str
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=32
    )
    confirm_password: str

class UserResponse(BaseModel):

    id:int
    name:str
    email:EmailStr
    role:UserRole

    class Config:
        
        from_attributes=True
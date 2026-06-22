from pydantic import BaseModel

class CustomerCreate(BaseModel):

    phone: str
    favorite_practitioner_id: int | None = None
    preferences: str | None = None

class CustomerResponse(BaseModel):

    id: int
    user_id: int
    phone: str
    favorite_practitioner_id: int | None = None
    preferences: str | None = None

    class Config:

        from_attributes=True
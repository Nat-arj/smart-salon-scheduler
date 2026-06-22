from pydantic import BaseModel

from app.core.enums import PaymentType

class PaymentCreate(BaseModel):

    appointment_id:int
    payment_type:PaymentType
    amount:float

class PaymentResponse(BaseModel):

    id:int
    appointment_id:int
    payment_type:PaymentType
    amount:float
    transaction_id:str | None=None

    class Config:

        from_attributes=True
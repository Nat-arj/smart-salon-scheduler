from pydantic import BaseModel

class ReviewCreate(BaseModel):

    appointment_id:int
    practitioner_id:int
    rating:float
    review_text:str | None=None

class ReviewResponse(BaseModel):

    id:int
    customer_id:int
    practitioner_id:int
    rating:float
    review_text:str | None=None

    class Config:

        from_attributes=True
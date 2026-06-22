from pydantic import BaseModel

class SalonResponse(BaseModel):

    id:int
    name:str
    address:str
    rating:float | None=None
    review_count:int | None=None
    is_active:bool

    class Config:

        from_attributes=True
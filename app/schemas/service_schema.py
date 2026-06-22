from pydantic import BaseModel

class ServiceCreate(BaseModel):

    name:str
    description:str
    duration_minutes:int
    base_price:float

class ServiceResponse(BaseModel):

    id:int
    name:str
    description:str
    duration_minutes:int
    base_price:float
    is_active:bool

    class Config:

        from_attributes=True
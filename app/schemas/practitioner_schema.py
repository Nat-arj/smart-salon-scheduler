from pydantic import BaseModel

class PractitionerCreate(BaseModel):

    salon_id:int
    name:str
    specialty:str
    experience:int

class PractitionerResponse(BaseModel):

    id:int
    salon_id:int
    user_id:int
    name:str
    specialty:str
    experience:int
    rating:float
    is_active:bool

    class Config:

        from_attributes=True
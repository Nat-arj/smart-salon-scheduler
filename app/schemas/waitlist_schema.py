from pydantic import BaseModel

from datetime import date
from datetime import time

class WaitlistCreate(BaseModel):

    practitioner_id:int
    preferred_date:date
    preferred_time:time

class WaitlistResponse(BaseModel):

    id:int
    customer_id:int
    practitioner_id:int
    preferred_date:date
    preferred_time:time
    notified:bool

    class Config:

        from_attributes=True
from pydantic import BaseModel

from datetime import date
from datetime import time

class AppointmentCreate(BaseModel):

    practitioner_id:int
    service_id:int
    appointment_date:date
    start_time:time

class AppointmentResponse(BaseModel):

    id:int
    customer_id:int
    practitioner_id:int
    service_id:int
    appointment_date:date
    start_time:time
    end_time:time

    class Config:

        from_attributes=True
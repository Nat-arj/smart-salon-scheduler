from pydantic import BaseModel

from datetime import date
from datetime import time

from app.core.enums import SlotStatus

class AvailabilityResponse(BaseModel):
    id: int
    practitioner_id: int
    slot_date: date
    start_time: time
    end_time: time
    status: SlotStatus

    class Config:
        from_attributes = True
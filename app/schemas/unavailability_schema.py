from pydantic import BaseModel

from datetime import date

from app.core.enums import LeaveType


class PractitionerUnavailabilityCreate(BaseModel):
    start_date: date
    end_date: date
    leave_type: LeaveType
    reason: str | None = None


class PractitionerUnavailabilityResponse(BaseModel):
    id: int
    practitioner_id: int
    start_date: date
    end_date: date
    leave_type: LeaveType
    reason: str | None = None

    class Config:
        from_attributes = True
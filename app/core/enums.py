from enum import Enum

class SlotStatus(str, Enum):

    AVAILABLE = "AVAILABLE"

    HOLD = "HOLD"

    BOOKED = "BOOKED"

    UNAVAILABLE = "UNAVAILABLE"

class AppointmentStatus(str, Enum):

    HELD = "HELD"

    BOOKED = "BOOKED"

    COMPLETED = "COMPLETED"

    CUSTOMER_CANCELLED = "CUSTOMER_CANCELLED"

    PRACTITIONER_CANCELLED = "PRACTITIONER_CANCELLED"

    RESCHEDULED = "RESCHEDULED"

    NO_SHOW = "NO_SHOW"

class PaymentStatus(str, Enum):

    PENDING = "PENDING"

    SUCCESS = "SUCCESS"

    FAILED = "FAILED"

    REFUNDED = "REFUNDED"

class Sentiment(str, Enum):

    POSITIVE = "POSITIVE"

    NEGATIVE = "NEGATIVE"

    NEUTRAL = "NEUTRAL"

class UserRole(str, Enum):

    CUSTOMER = "CUSTOMER"

    PRACTITIONER = "PRACTITIONER"

    ADMIN = "ADMIN"

class LeaveType(str, Enum):

    SICK="SICK"

    VACATION="VACATION"

    PERSONAL="PERSONAL"

    OTHER="OTHER"

class PaymentStatus(str, Enum):

    PENDING = "PENDING"

    SUCCESS = "SUCCESS"

    FAILED = "FAILED"

    REFUNDED = "REFUNDED"

class PaymentType(str, Enum):

    DEPOSIT = "DEPOSIT"

    FULL = "FULL"

    REMAINING = "REMAINING"

    REFUND = "REFUND"

    NO_SHOW_FEE = "NO_SHOW_FEE"


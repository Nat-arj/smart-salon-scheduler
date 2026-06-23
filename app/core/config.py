from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    DATABASE_URL = os.getenv("DATABASE_URL")

    DEPOSIT_PERCENTAGE: float = 0.20

    SLOT_DURATION: int = 30

settings = Settings()
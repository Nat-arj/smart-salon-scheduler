from fastapi import FastAPI

from app.db.database import Base
from app.db.database import engine

from app.routers.auth_router import router as auth_router
from app.routers.appointment_router import router as appointment_router 

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Smart Salon Scheduler",
    version="1.0.0"
)

app.include_router(auth_router)

app.include_router(appointment_router)

@app.get("/")
def home():
    return {
        "message": "Smart Salon Scheduler Running"
    }


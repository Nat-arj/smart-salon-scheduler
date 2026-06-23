from fastapi import FastAPI

from app.db.database import Base
from app.db.database import engine

from app.routers.auth_router import router 

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Smart Salon Scheduler",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Smart Salon Scheduler Running"
    }


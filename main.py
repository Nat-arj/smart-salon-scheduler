from fastapi import FastAPI

from app.db.database import Base
from app.db.database import engine

import app.models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Smart Salon Scheduler",
    version="1.0.0"
)


@app.get("/")
def home():

    return {

        "message": "Smart Salon Scheduler Running"

    }
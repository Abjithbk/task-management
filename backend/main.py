from fastapi import FastAPI, APIRouter

import models
from database import engine
from routers import tasks

models.Base.metadata.create_all(bind=engine)

router =APIRouter()

app = FastAPI(title="Task Management API")

app.include_router(tasks.router)


@app.get("/")
def root():
    return {"message": "Task Management API is running"}
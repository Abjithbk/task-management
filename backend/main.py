<<<<<<< HEAD
from fastapi import FastAPI, APIRouter

import models
from database import engine
from routers import tasks

models.Base.metadata.create_all(bind=engine)

router =APIRouter()

app = FastAPI(title="Task Management API")

app.include_router(tasks.router)
=======
from fastapi import FastAPI

import models
from database import engine
from routers import tasks, users

# Creates tasks.db and all tables if they don't exist yet
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

app.include_router(tasks.router)
app.include_router(users.router)
>>>>>>> 09ab0dd (Added user model and CRUD API with password hashing)


@app.get("/")
def root():
    return {"message": "Task Management API is running"}
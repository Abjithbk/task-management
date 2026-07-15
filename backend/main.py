from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []

class Task(BaseModel):
    title: str
    completed: bool = False


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    if task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    tasks[task_id] = task
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    deleted = tasks.pop(task_id)
    return deleted
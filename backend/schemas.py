from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(TaskBase):
    """Fields required to create a task."""
    pass


class TaskUpdate(BaseModel):
    """All fields optional — supports partial updates."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskResponse(TaskBase):
    id: int

    class Config:
        from_attributes = True
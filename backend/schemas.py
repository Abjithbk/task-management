from pydantic import BaseModel, EmailStr
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


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    """Plain password comes in here; it's hashed before hitting the DB."""
    password: str


class UserUpdate(BaseModel):
    """All fields optional — supports partial updates."""
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class UserResponse(UserBase):
    """Password is deliberately excluded — never send it back to the client."""
    id: int

    class Config:
        from_attributes = True
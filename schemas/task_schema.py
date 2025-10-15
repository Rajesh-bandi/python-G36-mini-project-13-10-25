from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class TaskBase(BaseModel):
    title: str = Field(..., example="Prepare monthly report")
    description: Optional[str] = Field(None, example="Collect sales and expense data.")
    status: TaskStatus = Field(TaskStatus.pending, example="pending")
    assigned_to: Optional[int] = Field(None, example=1)


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[TaskStatus]
    assigned_to: Optional[int]


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

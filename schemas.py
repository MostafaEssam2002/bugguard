from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime, timezone
from models import TaskStatus, TaskPriority

class TaskCreate(BaseModel):
    title: str = Field(..., max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: Optional[TaskStatus] = TaskStatus.pending
    priority: Optional[TaskPriority] = TaskPriority.medium
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = Field(default=None, max_length=100)
    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v):
        if not v or not v.strip():
            raise ValueError("Title must not be empty")
        return v.strip()
    @field_validator("due_date")
    @classmethod
    def due_date_in_future(cls, v):
        if v and v < datetime.now(timezone.utc):
            raise ValueError("Due date must be in the future")
        return v

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = Field(default=None, max_length=100)

class TaskResponse(TaskCreate):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = {
        "from_attributes": True
    }


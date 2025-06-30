from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime, timezone
from models import Task, TaskStatus, TaskPriority
from schemas import TaskCreate, TaskUpdate, TaskResponse
from database import get_session

router = APIRouter()
# POST /tasks - Create a new task
@router.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    db_task = Task.model_validate(task)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

# GET /tasks - List all tasks with optional filtering and pagination
@router.get("/tasks", response_model=List[TaskResponse])
def get_tasks(
    skip: int = 0,
    limit: int = 10,
    status: Optional[TaskStatus] = None,
    priority: Optional[TaskPriority] = None,
    search: Optional[str] = None,
    sort_by: Optional[str] = None,
    session: Session = Depends(get_session)
):
    query = select(Task)
    if status:
        query = query.where(Task.status == status)
    if priority:
        query = query.where(Task.priority == priority)
    if search:
        search_term = f"%{search}%"
        query = query.where(
            (Task.title.ilike(search_term)) |
            (Task.description.ilike(search_term))
        )
    if sort_by in ["title", "due_date", "created_at", "priority"]:
        query = query.order_by(getattr(Task, sort_by))
    query = query.offset(skip).limit(limit)
    tasks = session.exec(query).all()
    return tasks

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task_update.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    task.updated_at = datetime.now(timezone.utc)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return {"message": f"Task {task_id} deleted"}

@router.get("/tasks/status/{status}")
def get_tasks_by_status(status: TaskStatus, session: Session = Depends(get_session)):
    return session.exec(select(Task).where(Task.status == status)).all()

@router.get("/tasks/priority/{priority}")
def get_tasks_by_priority(priority: TaskPriority, session: Session = Depends(get_session)):
    return session.exec(select(Task).where(Task.priority == priority)).all()

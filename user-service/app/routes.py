from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db

# Initialize the router
router = APIRouter()

# Create a new taks endpoint
@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(title=task.title, description=task.description, status=task.status, due_date=task.due_date, created_at=task.created_at)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get a task by ID endpoint

@router.get("/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

# For products, the process is similar. Replace Task with Product and TaskCreate with ProductCreate.
# Create a new product endpoint


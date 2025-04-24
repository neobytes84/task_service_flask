from pydantic import BaseModel

# Define the taskcreate schema

class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: str
    status: str = "Pending"
    created_at: str = "auto"

# Define the task schema
class Task(BaseModel):
    id: int
    title: str
    description: str
    due_date: str
    status: str
    created_at: str
    
    class Config:
        orm_mode = True

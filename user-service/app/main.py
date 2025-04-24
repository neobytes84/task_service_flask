from fastapi import FastAPI
from flask import render_template
from .database import engine
from .models import Base
from .routes import router as task_router
from .routes import router as product_router
# Create all database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include the task router with the specified prefix and tags

app.include_router(task_router, prefix="/tasks", tags=["tasks"])
@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do API"}


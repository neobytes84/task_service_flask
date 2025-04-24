from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import router as user_router

# Create all database tables

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the User API"}
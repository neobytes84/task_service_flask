from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import router as product_router

# Create all database tables

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register the product routes

app.include_router(product_router, prefix="/products", tags=["products"])

@app.get("/")

def read_root():
    return {"message": "Welcome to the FastAPI Product API!"}
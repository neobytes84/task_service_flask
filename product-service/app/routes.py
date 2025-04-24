from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db

# Initialize the router

router = APIRouter()

# Create a new product endpoint

@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(name=product.name,price=product.price, quantity=product.quantity, category_id=product.category_id, supplier_id=product.supplier_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Get a task by ID endpoint

@router.get("/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
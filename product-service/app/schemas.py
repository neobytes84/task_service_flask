from pydantic import BaseModel

#Define the ProductCreate schema

class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int
    category_id: int
    supplier_id: int

# Define the Product schema

class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    category_id: int
    supplier_id: int
    
    class Config:
        orm_mode = True
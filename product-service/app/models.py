from sqlalchemy import Column, Integer, String
from .database import Base

# Define the Product model  
   
class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Integer)
    quantity = Column(Integer)
    category_id = Column(Integer, index=True)
    supplier_id = Column(Integer, index=True)
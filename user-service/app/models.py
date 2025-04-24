from sqlalchemy import Column, Float, Integer, String
from .database import Base

# Define the task model

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(String)
    due_date = Column(String)
    created_at = Column(String)

# Other models can be defined similarly...


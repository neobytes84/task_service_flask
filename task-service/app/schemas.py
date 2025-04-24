from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    email: str
    full_name: str
    password: str
    status : str = "active"

class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    password: str
    status: str = "active"
    
    class Config:
        orm_mode = True
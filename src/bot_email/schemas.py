from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    
    class Config:
        orm_mode = True

    
class UserResponse(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        orm_mode = True
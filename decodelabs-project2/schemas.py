from pydantic import BaseModel
from typing import Optional

# what the user sends when creating
class UserCreate(BaseModel):
    email: str
    age: int

# what the API returns
class UserResponse(BaseModel):
    id: int
    email: str
    age: int
    is_active: bool

    class Config:
        from_attributes = True
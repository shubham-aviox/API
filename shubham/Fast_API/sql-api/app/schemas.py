from typing import Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: Optional[int]
    is_active: bool = None
    items: list[Item] = []

    class Config:
        orm_mode = True
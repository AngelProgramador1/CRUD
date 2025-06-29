from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class ItemBase(BaseModel):
    title:str
    description: Optional[str]=None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id:int
    owner_id:int
    class config:
        orm_mode = True

class UserBase(BaseModel):
    email:EmailStr

class UserCreate(UserBase):
    password:str

class User(UserBase):
    id:int
    is_active:bool
    created_at: datetime
    items: List[Item] = []
    class config:
        orm_mode = True

    
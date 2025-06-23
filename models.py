from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email= Column(String,unique=True, index=True)
    hashed_password= Column(String)
    is_active= Column(Boolean,default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    items = relationship("Item",back_populates="owner")

class Item(Base):
    __tablename__ = "items"
    id= Column(Integer,primary_key=True,index=True)
    title= Column(String, index=True)
    description= Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User",back_populates="items")
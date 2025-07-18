from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, models
from database import  SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind= engine)
def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close_all()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_users_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="email already registered")
    return crud.create_user(db= db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip= skip, limit= limit)
    return users

def numero():
    return 2

@app.get("/")
def get(db: int = Depends(numero)):
    return {"el resultado es": 2} if db == 2 else "nada"
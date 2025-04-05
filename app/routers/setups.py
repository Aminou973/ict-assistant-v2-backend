# setups.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter(prefix="/setups", tags=["Setups"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Setup)
def create_setup(setup: schemas.SetupCreate, db: Session = Depends(get_db)):
    return crud.create_setup(db, setup)

@router.get("/user/{user_id}", response_model=list[schemas.Setup])
def get_user_setups(user_id: int, db: Session = Depends(get_db)):
    return crud.get_setups_by_user(db, user_id)

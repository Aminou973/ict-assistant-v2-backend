# journal.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter(prefix="/journal", tags=["Journal"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.JournalEntry)
def create_journal(entry: schemas.JournalEntryCreate, db: Session = Depends(get_db)):
    return crud.create_journal_entry(db, entry)

@router.get("/user/{user_id}", response_model=list[schemas.JournalEntry])
def get_user_journal(user_id: int, db: Session = Depends(get_db)):
    return crud.get_journal_by_user(db, user_id)

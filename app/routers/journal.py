
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.JournalEntry)
def create_journal_entry(entry: schemas.JournalEntryBase, db: Session = Depends(get_db)):
    db_entry = models.JournalEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.JournalEntry)
def create_journal_entry(entry: schemas.JournalEntryCreate, db: Session = Depends(get_db)):
    return crud.create_journal_entry(db, entry)

@router.get("/", response_model=List[schemas.JournalEntry])
def get_all_journal_entries(db: Session = Depends(get_db)):
    return crud.get_journal_entries(db)
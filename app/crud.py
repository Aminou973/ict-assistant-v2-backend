from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

def create_setup(db: Session, setup: schemas.SetupCreate):
    db_setup = models.Setup(**setup.dict(), created_at=datetime.utcnow())
    db.add(db_setup)
    db.commit()
    db.refresh(db_setup)
    return db_setup

def get_setups(db: Session):
    return db.query(models.Setup).order_by(models.Setup.created_at.desc()).all()

def create_journal_entry(db: Session, entry: schemas.JournalEntryCreate):
    db_entry = models.JournalEntry(**entry.dict(), created_at=datetime.utcnow())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_journal_entries(db: Session):
    return db.query(models.JournalEntry).order_by(models.JournalEntry.created_at.desc()).all()
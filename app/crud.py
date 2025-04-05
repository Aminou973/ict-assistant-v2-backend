
from sqlalchemy.orm import Session
from app import models

def create_setup(db: Session, setup_data):
    db_setup = models.Setup(**setup_data.dict())
    db.add(db_setup)
    db.commit()
    db.refresh(db_setup)
    return db_setup

def get_setups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Setup).offset(skip).limit(limit).all()

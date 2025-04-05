from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models, crud
from app.database import get_db
from app.utils.discord_bot import send_signal_to_discord

router = APIRouter()

@router.post("/", response_model=schemas.Setup)
def create_setup(setup: schemas.SetupCreate, db: Session = Depends(get_db)):
    new_setup = crud.create_setup(db, setup)
    send_signal_to_discord(setup)
    return new_setup

@router.get("/", response_model=List[schemas.Setup])
def read_setups(db: Session = Depends(get_db)):
    return crud.get_setups(db)
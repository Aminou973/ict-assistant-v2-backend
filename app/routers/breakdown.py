from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import BreakdownCreate, Breakdown
from app.database import get_db
from app import models

router = APIRouter(
    prefix="/breakdown",
    tags=["Breakdown"]
)

@router.post("/", response_model=Breakdown)
def create_breakdown(entry: BreakdownCreate, db: Session = Depends(get_db)):
    db_entry = models.Breakdown(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.get("/", response_model=list[Breakdown])
def get_all_breakdowns(db: Session = Depends(get_db)):
    return db.query(models.Breakdown).order_by(models.Breakdown.created_at.desc()).all()
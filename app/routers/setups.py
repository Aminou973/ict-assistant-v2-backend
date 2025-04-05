# setups.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal
from app.utils.discord_bot import send_signal_to_discord  # ajoute en haut

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


@router.post("/", response_model=schemas.Setup)
def create_setup(setup: schemas.SetupCreate, db: Session = Depends(get_db)):
    created_setup = crud.create_setup(db, setup)

    # Format du message Discord
    title = f"📈 Nouveau setup ICT sur {created_setup.symbol}"
    message = (
        f"🧠 Contexte : {created_setup.context}\n"
        f"🎯 Entry : {created_setup.entry_price} | SL : {created_setup.stop_loss} | TP : {created_setup.take_profit}\n"
        f"📊 RR : {created_setup.risk_reward}"
    )

    # Envoi vers Discord
    send_signal_to_discord(message, title)

    return created_setup

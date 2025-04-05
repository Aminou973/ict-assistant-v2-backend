from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.discord_bot import send_signal_to_discord

router = APIRouter(prefix="/signals", tags=["Signals"])

class SignalRequest(BaseModel):
    title: str
    message: str

@router.post("/manual")
def send_manual_signal(req: SignalRequest):
    send_signal_to_discord(req.message, req.title)
    return {"status": "Signal envoyé à Discord"}

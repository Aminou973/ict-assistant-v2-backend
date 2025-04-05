from fastapi import APIRouter
from app.utils.discord_bot import send_signal_to_discord

router = APIRouter(prefix="/test-discord", tags=["Discord"])

@router.get("/")
def send_test_message():
    send_signal_to_discord("🚨 Test ICT signal envoyé depuis le backend !")
    return {"message": "Signal envoyé à Discord"}

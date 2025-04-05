# app/routers/alerts.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SetupCreate(BaseModel):
    symbol: str
    context: str
    entry_price: float
    stop_loss: float
    take_profit: float
    risk_reward: float
    probability_score: float
    bias: str
    confidence_comment: str

@router.post("/tv")
async def receive_tv_alert(setup: SetupCreate):
    print(setup.dict())
    return {"status": "received", "setup": setup}

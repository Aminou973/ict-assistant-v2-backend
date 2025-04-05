from fastapi import APIRouter
from app.schemas import Stats
from datetime import datetime

router = APIRouter()

@router.get("/", response_model=Stats)
def get_stats():
    # Valeurs simulées pour test
    return Stats(
        total_trades=42,
        win_rate=78.5,
        average_rr=2.3,
        best_setup="SSLQ + MSS + OB NY PM",
        last_updated=datetime.utcnow()
    )
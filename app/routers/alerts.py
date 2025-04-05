from fastapi import APIRouter, Request
import json
import logging

router = APIRouter()

@router.post("/alerts/tv")
async def receive_tv_alert(request: Request):
    try:
        data = await request.json()
        logging.info("✅ Alert received from TradingView: %s", data)
        # Ici tu peux traiter l’alerte, par exemple :
        symbol = data.get("ticker") or data.get("symbol")
        message = data.get("message", "No message provided")
        print(f"[📡 ALERTE] {symbol}: {message}")
        return {"status": "success", "message": "Alert received"}
    except Exception as e:
        logging.error(f"❌ Failed to parse TV alert: {e}")
        return {"status": "error", "message": str(e)}

from fastapi import APIRouter, Request
import json
import logging

router = APIRouter()

@router.post("/alerts/tv")
async def receive_tv_alert(request: Request):
    try:
        data = await request.json()
        logging.info("✅ Alert received from TradingView: %s", data)
        ...
    except Exception as e:
        body = await request.body()
        logging.error(f"❌ Failed to parse TV alert: {e} | Raw body: {body}")
        return {"status": "error", "message": str(e)}


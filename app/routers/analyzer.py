
from fastapi import APIRouter
from app.core.assistant import analyse_setup_conditions

router = APIRouter()

@router.post("/analyze/")
def analyze_setup(setup: dict):
    result = analyse_setup_conditions(setup)
    return result

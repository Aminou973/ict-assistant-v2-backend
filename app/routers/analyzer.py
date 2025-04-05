from fastapi import APIRouter
from app.schemas import AnalyzeRequest, AnalyzeResponse
from app.utils.analyze_local import analyze_setup_local

router = APIRouter()

@router.post("/", response_model=AnalyzeResponse)
def analyze_setup(request: AnalyzeRequest):
    return analyze_setup_local(request)
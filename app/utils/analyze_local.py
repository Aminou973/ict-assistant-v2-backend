from app.schemas import AnalyzeRequest, AnalyzeResponse

def analyze_setup_local(setup: AnalyzeRequest) -> AnalyzeResponse:
    score = 0.5
    comment = "Base setup"

    if "SSLQ" in setup.context.upper():
        score += 0.2
        comment = "Includes SSLQ"
    if "MSS" in setup.context.upper():
        score += 0.15
        comment += " + MSS Confirmed"
    if setup.risk_reward >= 2:
        score += 0.1
        comment += " + Good RR"

    score = round(min(score, 1.0), 2)

    return AnalyzeResponse(
        probability_score=score,
        bias="Bullish" if score > 0.6 else "Bearish",
        confidence_comment=comment
    )

def analyse_setup_conditions(setup: dict) -> dict:
    symbol = setup.get("symbol", "")
    context = setup.get("context", "").lower()
    session = setup.get("session", "").lower()

    confidence = 0
    alerts = []
    reasoning = []

    if "sslq" in context or "liquidity sweep" in context:
        confidence += 25
        alerts.append("Liquidity Sweep détecté")
        reasoning.append("Sweep détecté dans le contexte")

    if "mss" in context or "market structure shift" in context:
        confidence += 25
        alerts.append("MSS confirmé")
        reasoning.append("Changement de structure détecté")

    if "ob" in context or "order block" in context:
        confidence += 15
        reasoning.append("Présence d’un Order Block")

    if "fvg" in context:
        confidence += 10
        reasoning.append("Fair Value Gap identifié")

    if session in ["london", "new york am", "ny pm", "power hour"]:
        confidence += 20
        reasoning.append(f"Session favorable : {session.title()}")

    if confidence >= 80:
        recommendation = "Trade fortement recommandé"
    elif confidence >= 60:
        recommendation = "Trade possible avec bon contexte"
    elif confidence >= 40:
        recommendation = "Contexte moyen - prudence"
    else:
        recommendation = "Éviter le trade"

    return {
        "confidence_score": confidence,
        "recommendation": recommendation,
        "alerts": alerts,
        "reasoning": reasoning
    }

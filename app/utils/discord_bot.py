import requests
import os

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_signal_to_discord(setup_data: dict):
    if not DISCORD_WEBHOOK_URL:
        print("❌ Webhook Discord manquant")
        return

    message = (
        f"📡 **Nouvelle alerte TradingView reçue**\n"
        f"**Symbol**: {setup_data.get('symbol')}\n"
        f"**Contexte**: {setup_data.get('context')}\n"
        f"**Prix entrée**: {setup_data.get('entry_price')}\n"
        f"**SL / TP**: {setup_data.get('stop_loss')} → {setup_data.get('take_profit')}\n"
        f"**RR**: {setup_data.get('risk_reward')} | 🎯 Probabilité: {setup_data.get('probability_score')}\n"
        f"**Bias**: {setup_data.get('bias')}\n"
        f"🧠 {setup_data.get('confidence_comment')}"
    )

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json={"content": message})
        response.raise_for_status()
        print("✅ Alerte envoyée sur Discord")
    except Exception as e:
        print(f"❌ Erreur envoi Discord: {e}")

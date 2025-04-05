import requests
import os

# Webhook du channel #signals (remplace ici si tu en ajoutes d'autres)
DISCORD_SIGNALS_WEBHOOK = os.getenv("DISCORD_SIGNALS_WEBHOOK")

def send_signal_to_discord(message: str):
    if not DISCORD_SIGNALS_WEBHOOK:
        raise ValueError("DISCORD_SIGNALS_WEBHOOK is not set in .env")

    data = {
        "content": message
    }
    response = requests.post(DISCORD_SIGNALS_WEBHOOK, json=data)
    if response.status_code != 204:
        raise Exception(f"Erreur envoi Discord: {response.status_code} - {response.text}")

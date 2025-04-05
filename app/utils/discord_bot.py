import requests
import os

DISCORD_SIGNALS_WEBHOOK = os.getenv("DISCORD_SIGNALS_WEBHOOK")

def send_signal_to_discord(message: str, title: str = "🚨 Signal ICT détecté"):
    if not DISCORD_SIGNALS_WEBHOOK:
        raise ValueError("DISCORD_SIGNALS_WEBHOOK is not set in .env")

    embed = {
        "title": title,
        "description": message,
        "color": 0xE91E63  # rose flashy
    }

    data = {
        "embeds": [embed]
    }

    response = requests.post(DISCORD_SIGNALS_WEBHOOK, json=data)
    if response.status_code != 204:
        raise Exception(f"Erreur Discord: {response.status_code} - {response.text}")

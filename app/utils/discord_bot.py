
import requests
import os

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "https://discordapp.com/api/webhooks/...")

def send_signal_to_discord(setup):
    message = {
        "content": f"📈 Signal détecté : {setup.symbol}\n📌 Contexte : {setup.context}\n🎯 Entry: {setup.entry_price} | TP: {setup.take_profit} | SL: {setup.stop_loss}"
    }
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=message)
    except Exception as e:
        print("Erreur Discord:", e)

import requests
from app.schemas import SetupCreate

DISCORD_WEBHOOK_URL = "https://discordapp.com/api/webhooks/1358046429616148480/c4RFindu8sWCSfqcLBeH4Zw-8iHCCHe7yrN7ci_OV1EhFD82RVPAC-B6eBZPozi3YtjF"

def send_signal_to_discord(setup_data: SetupCreate):
    message = {
        "content": (
            f"📈 **New Setup Logged**\n\n"
            f"**Symbol**: {setup_data.symbol}\n"
            f"**Context**: {setup_data.context}\n"
            f"**Entry**: {setup_data.entry_price}\n"
            f"**SL**: {setup_data.stop_loss}\n"
            f"**TP**: {setup_data.take_profit}\n"
            f"**RR**: {setup_data.risk_reward}\n"
            f"**Bias**: {getattr(setup_data, 'bias', 'N/A')}\n"
            f"**Probability**: {getattr(setup_data, 'probability_score', 'N/A')}\n"
            f"**Comment**: {getattr(setup_data, 'confidence_comment', 'N/A')}"
        )
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=message)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message to Discord: {e}")

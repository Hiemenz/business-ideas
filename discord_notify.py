import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


def post(message: str, username: str = "Pi Bot") -> bool:
    if not WEBHOOK_URL:
        return False
    payload = {"content": message, "username": username}
    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=15)
    except requests.RequestException:
        return False
    return response.status_code == 204


if __name__ == "__main__":
    post("Hello from the Pi!")

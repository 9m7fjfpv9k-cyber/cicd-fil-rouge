"""Notifications sortantes (Slack, Teams...) via un webhook."""

import requests

from app import settings


def notify(message: str) -> bool:
    """Envoie un message sur le webhook configuré. Ne fait rien si aucun webhook."""
    if not settings.NOTIFY_WEBHOOK_URL:
        return False
    response = requests.post(settings.NOTIFY_WEBHOOK_URL, json={"text": message}, timeout=5)
    return response.ok

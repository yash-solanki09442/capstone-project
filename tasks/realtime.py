import os

import requests

REALTIME_SERVICE_URL = os.getenv("REALTIME_SERVICE_URL", "http://127.0.0.1:8080")


def broadcast_event(event: dict) -> None:
    """
    Best-effort: do not break the main API if realtime service is down.
    """
    url = f"{REALTIME_SERVICE_URL}/broadcast"
    try:
        requests.post(url, json=event, timeout=2)
    except requests.RequestException:
        return

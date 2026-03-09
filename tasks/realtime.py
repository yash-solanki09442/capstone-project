import os

import requests
import structlog

logger = structlog.get_logger(__name__)

REALTIME_SERVICE_URL = os.getenv("REALTIME_SERVICE_URL", "http://127.0.0.1:8080")


def broadcast_event(event: dict) -> None:
    url = f"{REALTIME_SERVICE_URL}/broadcast"
    try:
        response = requests.post(url, json=event, timeout=2)
        response.raise_for_status()

        logger.info(
            "realtime_broadcast_sent",
            event_type=event.get("type"),
            task_id=event.get("task_id"),
            project_id=event.get("project_id"),
            status_code=response.status_code,
        )
    except requests.RequestException as exc:
        logger.error(
            "realtime_broadcast_failed",
            event_type=event.get("type"),
            task_id=event.get("task_id"),
            project_id=event.get("project_id"),
            error=str(exc),
        )

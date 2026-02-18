from typing import Protocol


class Notifier(Protocol):
    def send(self, to: str, msg: str) -> None: ...


class EmailClient:
    def send(self, to: str, msg: str) -> None:
        print(f"Sending email to {to}: {msg}")


class NotificationService:
    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier

    def notify(self, to: str, msg: str) -> None:
        self.notifier.send(to, msg)

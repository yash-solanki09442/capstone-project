class EmailClient:
    def send(self, to: str, msg: str) -> None:
        print(f"Sending email to {to}: {msg}")


class NotificationService:
    def __init__(self) -> None:
        self.client = EmailClient()

    def notify(self, to: str, msg: str) -> None:
        self.client.send(to, msg)

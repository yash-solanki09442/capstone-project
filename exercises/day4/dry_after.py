def _send_email(user_email: str, message: str) -> None:
    print("Connecting to SMTP server...")
    print("Authenticating...")
    print(f"Sending email to {user_email}: {message}")


def send_welcome_email(user_email: str) -> None:
    _send_email(user_email, "Welcome!")


def send_password_reset_email(user_email: str) -> None:
    _send_email(user_email, "Reset your password.")

def send_welcome_email(user_email: str) -> None:
    print(f"Connecting to SMTP server...")
    print(f"Authenticating...")
    print(f"Sending email to {user_email}: Welcome!")


def send_password_reset_email(user_email: str) -> None:
    print(f"Connecting to SMTP server...")
    print(f"Authenticating...")
    print(f"Sending email to {user_email}: Reset your password.")

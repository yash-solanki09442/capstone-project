def send_welcome_email(user_email: str) -> None:
    print("Connecting to SMTP server...")
    print("Authenticating...")
    print(f"Sending email to {user_email}: Welcome!")


def send_password_reset_email(user_email: str) -> None:
    print("Connecting to SMTP server...")
    print("Authenticating...")
    print(f"Sending email to {user_email}: Reset your password.")

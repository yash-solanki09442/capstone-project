def calculate_discount(user_type: str, amount: float) -> float:
    if user_type == "regular":
        return amount * 0.95
    if user_type == "premium":
        return amount * 0.90
    raise ValueError("Unknown user type")

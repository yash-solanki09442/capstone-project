import re


def slugify(text: str) -> str:
    # normalize
    text = text.strip().lower()

    # remove special characters (keep letters/numbers/spaces/hyphens)
    text = re.sub(r"[^a-z0-9\s-]", "", text)

    # collapse whitespace to single hyphen
    text = re.sub(r"\s+", "-", text)

    # collapse multiple hyphens (defensive)
    text = re.sub(r"-{2,}", "-", text)

    # remove leading/trailing hyphens (defensive)
    return text.strip("-")

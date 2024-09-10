def is_correct_email(raw_email: str) -> bool:
    raw_email_parts = raw_email.split("@")
    if len(raw_email_parts) != 2:
        return False
    _, right_part = raw_email_parts
    if not right_part:
        return False
    return len(right_part.split(".")) > 1


if __name__ == "__main__":
    assert is_correct_email(raw_email="test@gmail.co") is True

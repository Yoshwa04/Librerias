import re

def is_email(text: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, text) is not None


def is_url(text: str) -> bool:
    pattern = r"^(https?://)?([\w\-]+\.)+[\w\-]+(/[\w\-./?%&=]*)?$"
    return re.match(pattern, text) is not None


def is_number(text: str) -> bool:
    return text.replace(".", "", 1).isdigit()


def is_integer(text: str) -> bool:
    return text.isdigit()


def has_only_letters(text: str) -> bool:
    return text.isalpha()


def has_only_alphanumeric(text: str) -> bool:
    return text.isalnum()

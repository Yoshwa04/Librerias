import re

def is_email(text: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, text) is not None


def is_url(text: str) -> bool:
    pattern = r"^(https?://)?([\w\-]+\.)+[\w\-]+(/[\w\-./?%&=]*)?$"
    return re.match(pattern, text) is not None

def is_valid_dni(text: str) -> bool:
    pattern = r"^\d{8}[A-Za-z]$"
    
    if not re.match(pattern, text):
        return False
    
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    number = int(text[:-1])
    letter = text[-1].upper()
    
    return letters[number % 23] == letter

def is_number(text: str) -> bool:
    return text.replace(".", "", 1).isdigit()


def is_integer(text: str) -> bool:
    return text.isdigit()


def has_only_letters(text: str) -> bool:
    return text.isalpha()


def has_only_alphanumeric(text: str) -> bool:
    return text.isalnum()

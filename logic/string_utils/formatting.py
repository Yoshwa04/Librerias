def to_upper(text: str) -> str:
    return text.upper()


def to_lower(text: str) -> str:
    return text.lower()


def capitalize_text(text: str) -> str:
    return text.capitalize()


def title_case(text: str) -> str:
    return text.title()


def remove_extra_spaces(text: str) -> str:
    return " ".join(text.split())


def reverse_text(text: str) -> str:
    return text[::-1]


def repeat_text(text: str, times: int) -> str:
    return text * times

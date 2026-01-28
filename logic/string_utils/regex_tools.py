import re

def find_all(pattern: str, text: str) -> list:
    return re.findall(pattern, text)


def replace(pattern: str, replacement: str, text: str) -> str:
    return re.sub(pattern, replacement, text)


def starts_with(pattern: str, text: str) -> bool:
    return re.match(pattern, text) is not None


def contains(pattern: str, text: str) -> bool:
    return re.search(pattern, text) is not None


def split_by_pattern(pattern: str, text: str) -> list:
    return re.split(pattern, text)

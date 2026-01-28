def count_characters(text: str) -> int:
    return len(text)


def count_letters(text: str) -> int:
    return sum(1 for c in text if c.isalpha())


def count_words(text: str) -> int:
    return len(text.split())


def count_sentences(text: str) -> int:
    return text.count(".") + text.count("!") + text.count("?")


def count_vowels(text: str) -> int:
    vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for c in text if c in vowels)


def count_consonants(text: str) -> int:
    return sum(1 for c in text if c.isalpha() and c.lower() not in "aeiouáéíóú")

def write_text_file(path: str, content: str):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def append_text_file(path: str, content: str):
    with open(path, "a", encoding="utf-8") as file:
        file.write(content)


def write_binary_file(path: str, content: bytes):
    with open(path, "wb") as file:
        file.write(content)

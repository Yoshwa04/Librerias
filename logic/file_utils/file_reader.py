def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def read_lines(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def read_binary_file(path: str) -> bytes:
    with open(path, "rb") as file:
        return file.read()

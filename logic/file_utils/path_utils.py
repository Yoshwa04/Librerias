import os

def exists(path: str) -> bool:
    return os.path.exists(path)


def is_file(path: str) -> bool:
    return os.path.isfile(path)


def is_directory(path: str) -> bool:
    return os.path.isdir(path)


def create_directory(path: str):
    os.makedirs(path, exist_ok=True)


def get_filename(path: str) -> str:
    return os.path.basename(path)


def get_extension(path: str) -> str:
    return os.path.splitext(path)[1]


def join_paths(*paths) -> str:
    return os.path.join(*paths)


def list_files(path: str) -> list:
    return os.listdir(path)


def get_absolute_path(path: str) -> str:
    return os.path.abspath(path)

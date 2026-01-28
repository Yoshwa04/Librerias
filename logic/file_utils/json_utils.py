import json
from typing import Any, Dict


def load_json(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(path: str, data: dict, indent: int = 4):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=indent, ensure_ascii=False)

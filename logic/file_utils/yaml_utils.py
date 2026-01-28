import yaml
from typing import Any, Dict


def load_yaml(filepath: str) -> Dict[str, Any]:
    """
    Loads a YAML file and returns it as a dictionary.

    Args:
        filepath: Path to the YAML file.

    Returns:
        dict: Parsed YAML data.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
from typing import Any, List, Dict, Optional

def to_int(value: Any, default: Optional[int] = None) -> Optional[int]:
    """
    Converts a value to int, returns default if conversion fails.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def to_float(value: Any, default: Optional[float] = None) -> Optional[float]:
    """
    Converts a value to float, returns default if conversion fails.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def to_str(value: Any, default: Optional[str] = None) -> Optional[str]:
    """
    Converts a value to string, returns default if conversion fails.
    """
    try:
        return str(value)
    except Exception:
        return default

def to_list(value: Any, default: Optional[List[Any]] = None) -> Optional[List[Any]]:
    """
    Converts a value to a list if possible, otherwise returns default.
    """
    if isinstance(value, list):
        return value
    elif value is None:
        return default
    else:
        return [value]

def to_dict(value: Any, default: Optional[Dict[Any, Any]] = None) -> Optional[Dict[Any, Any]]:
    """
    Converts a value to a dict if possible, otherwise returns default.
    """
    if isinstance(value, dict):
        return value
    else:
        return default

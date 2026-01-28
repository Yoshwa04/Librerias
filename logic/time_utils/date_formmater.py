from datetime import datetime

def get_current_datetime() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_current_date() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def get_current_time() -> str:
    return datetime.now().strftime("%H:%M:%S")


def format_date(date_obj: datetime, format_str: str) -> str:
    return date_obj.strftime(format_str)


def string_to_date(date_string: str, format_str: str) -> datetime:
    return datetime.strptime(date_string, format_str)


def days_between(date1: datetime, date2: datetime) -> int:
    return abs((date2 - date1).days)

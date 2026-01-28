from datetime import datetime
import pytz

def convert_timezone(date_time: datetime, from_tz: str, to_tz: str) -> datetime:
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)

    localized_time = from_zone.localize(date_time)
    return localized_time.astimezone(to_zone)


def get_time_in_timezone(timezone: str) -> str:
    tz = pytz.timezone(timezone)
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

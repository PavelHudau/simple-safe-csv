import datetime as dt
from typing import Union


class TestModel:
    __test__ = False

    def __init__(
            self,
            int_field: Union[int, str] = None,
            string_field: str = None,
            datetime_field: Union[dt.datetime, str] = None):
        self.int_field: int = _to_int_or_none(int_field)
        self.string_field: str = string_field
        self.datetime_field: dt.datetime = _to_date_time_or_none(
            datetime_field)


def _to_date_time_or_none(value: Union[dt.datetime, str]) -> dt.datetime:
    if isinstance(value, str):
        return dt.datetime.fromisoformat(value) if value else None
    return value


def _to_int_or_none(value: Union[int, str]) -> int:
    if isinstance(value, str):
        return int(value) if value else None
    return value

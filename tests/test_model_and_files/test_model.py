import datetime as dt
from typing import Union


class TestModel:
    __test__ = False

    def __init__(
            self,
            int_field: int = None,
            string_field: str = None,
            datetime_field: dt.datetime = None):
        self.int_field: int = _to_int_or_none(int_field)
        self.string_field: str = string_field
        self.datetime_field: dt.datetime = _to_date_time_or_none(
            datetime_field)


def _to_date_time_or_none(value: Union[str, dt.datetime]) -> dt.datetime:
    if isinstance(value, str):
        return dt.datetime.fromisoformat(value) if value else None
    return value


def _to_int_or_none(value: Union[str, int]) -> int:
    if isinstance(value, str):
        return int(value) if value else None
    return value

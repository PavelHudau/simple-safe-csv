import datetime as dt
from typing import List

import pytz
import src.csv_gen as csv_gen

from .test_model_and_files import test_model as tm


def test_read_valid_file_has_header():
    # GIVEN
    path = "./tests/test_model_and_files/test_valid_with_header.csv"

    # WHEN
    data: List[tm.TestModel] = csv_gen.read_from_csv(path, tm.TestModel)

    # THEN
    assert len(data) == 5

    assert data[0].int_field == 1
    assert data[0].string_field == "hello 1"
    assert data[0].datetime_field == dt.datetime(
        2020, 10, 30, 10, 41, 45, 968627)

    assert data[1].int_field == 2
    assert data[1].string_field == "hello 2"
    assert data[1].datetime_field == dt.datetime(
        2020, 10, 30, 10, 42, 49, 559897, tzinfo=pytz.UTC)

    assert data[2].int_field == 3
    assert data[2].string_field == "hello 3"
    assert data[2].datetime_field is None

    assert data[3].int_field == 4
    assert data[3].string_field == ""
    assert data[3].datetime_field == dt.datetime(
        2020, 10, 30, 10, 41, 45, 968627)

    assert data[4].int_field is None
    assert data[4].string_field == "hello 5"
    assert data[4].datetime_field == dt.datetime(
        2020, 10, 30, 10, 41, 45, 968627)


def test_read_valid_file_no_header():
    # GIVEN
    path = "./tests/test_model_and_files/test_valid_without_header.csv"

    # WHEN
    data: List[tm.TestModel] = csv_gen.read_from_csv(
        path,
        tm.TestModel,
        has_header=False)

    # THEN
    assert len(data) == 5

    assert data[0].int_field == 1
    assert data[0].string_field == "hello 1"
    assert data[0].datetime_field == dt.datetime(
        2020, 10, 30, 10, 41, 45, 968627)

    assert data[1].int_field == 2
    assert data[1].string_field == "hello 2"
    assert data[1].datetime_field == dt.datetime(
        2020, 10, 30, 10, 42, 49, 559897, tzinfo=pytz.UTC)

    assert data[2].int_field == 3
    assert data[2].string_field == "hello 3"
    assert data[2].datetime_field is None

    assert data[3].int_field == 4
    assert data[3].string_field == ""
    assert data[3].datetime_field == dt.datetime(
        2020, 10, 30, 10, 41, 45, 968627)

    assert data[4].int_field is None
    assert data[4].string_field == "hello 5"
    assert data[4].datetime_field == dt.datetime(
        2020, 10, 30, 10, 41, 45, 968627)

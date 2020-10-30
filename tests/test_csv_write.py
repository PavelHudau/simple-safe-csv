import csv
import datetime as dt
import os
from typing import Union

import pytest
import pytz
import src.csv_gen as csv_gen

from .test_model_and_files import test_model as tm


def test_file_generation_with_auto_columns(tmp_path):
    # GIVEN
    utc_now = pytz.utc.localize(dt.datetime.utcnow())
    utc_now_plus_1 = utc_now + dt.timedelta(days=1)
    data = [
        tm.TestModel(int_field=1, string_field="1", datetime_field=utc_now),
        tm.TestModel(int_field=2, string_field="2",
                     datetime_field=utc_now_plus_1),
    ]
    test_file_name = os.path.join(tmp_path, __name__)

    # WHEN
    csv_gen.write_as_csv(test_file_name, data)

    # THEN
    rows = []
    with open(test_file_name, 'r', newline='') as file:
        reader = csv.DictReader(
            file,
            fieldnames=["int_field", "string_field", "datetime_field"])
        rows = [row for row in reader]

    assert "int_field" == rows[0]["int_field"]
    assert "string_field" == rows[0]["string_field"]
    assert "datetime_field" == rows[0]["datetime_field"]

    assert str(data[0].int_field) == rows[1]["int_field"]
    assert data[0].string_field == rows[1]["string_field"]
    assert data[0].datetime_field.isoformat() == rows[1]["datetime_field"]

    assert str(data[1].int_field) == rows[2]["int_field"]
    assert data[1].string_field == rows[2]["string_field"]
    assert data[1].datetime_field.isoformat() == rows[2]["datetime_field"]


def test_file_generation_with_specified_columns(tmp_path):
    # GIVEN
    utc_now = pytz.utc.localize(dt.datetime.utcnow())
    utc_now_plus_1 = utc_now + dt.timedelta(days=1)
    data = [
        tm.TestModel(int_field=1, string_field="1", datetime_field=utc_now),
        tm.TestModel(int_field=2, string_field="2",
                     datetime_field=utc_now_plus_1),
    ]
    test_file_name = os.path.join(tmp_path, __name__)

    # WHEN
    csv_gen.write_as_csv(test_file_name, data, columns=[
        "int_field", "datetime_field"])

    # THEN
    rows = []
    with open(test_file_name, 'r', newline='') as file:
        reader = csv.DictReader(
            file,
            fieldnames=["int_field", "datetime_field"])
        rows = [row for row in reader]

    assert "int_field" == rows[0]["int_field"]
    assert "datetime_field" == rows[0]["datetime_field"]
    assert "string_field" not in rows[0]

    assert str(data[0].int_field) == rows[1]["int_field"]
    assert data[0].datetime_field.isoformat() == rows[1]["datetime_field"]
    assert "string_field" not in rows[1]

    assert str(data[1].int_field) == rows[2]["int_field"]
    assert data[1].datetime_field.isoformat() == rows[2]["datetime_field"]
    assert "string_field" not in rows[2]

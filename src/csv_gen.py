import csv
import datetime as dt
from typing import List


def write_as_csv(file_path: str, data: List[object], columns: List[str] = []):
    if not data:
        raise ValueError("data is empty or None")
    if not columns:
        # Infer columns from the first item in data
        first_item = data[0]
        columns = [key for key, _ in first_item.__dict__.items()]

    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(
            file,
            fieldnames=columns,
            extrasaction="ignore")
        writer.writeheader()
        writer.writerows([_to_json_safe_dict(data_item) for data_item in data])


def read_from_csv(file_path: str, type_to_read: type, has_header=True, columns: List[str] = []):
    if not type_to_read and not columns:
        raise ValueError("dattype_to_read or columns is needed")
    if not columns:
        # Infer columns from type_to_read
        item_to_read = type_to_read()
        columns = [key for key, _ in item_to_read.__dict__.items()]

    rows = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(
            file,
            fieldnames=columns)
        rows = [row for row in reader]
    
    skip_header = has_header
    data = []
    for row in rows:
        if skip_header:
            skip_header = False
            continue
        data.append(type_to_read(**row))
    
    return data



def _to_json_safe_dict(obj: object, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = _to_json_safe_dict(v, classkey)
        return data
    if isinstance(obj, (dt.datetime, dt.date)):
        return obj.isoformat()
    if hasattr(obj, "_ast"):
        return _to_json_safe_dict(obj._ast())
    if hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [_to_json_safe_dict(v, classkey) for v in obj]
    if hasattr(obj, "__dict__"):
        data = {
            k: _to_json_safe_dict(v, classkey)
            for k, v in obj.__dict__.items()
            if not callable(v) and not k.startswith("_")
        }
        if classkey and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    return obj

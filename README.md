# simple-safe-csv
Simple and type safe approach to generating CSV files with Python

## How to use

### Create a type-safe model class
Minimum requirements are
1. Constructor must take all field values as named parameters.
1. Value that comes as constructor argument can be either of exact type or a string. Before assigning the valueto a model field need to convert it from string if neessary.

#### Model Example
```py
class Model:
    def __init__(
            self,
            int_field: int = None,
            string_field: str = None,
            datetime_field: dt.datetime = None):
        self.int_field: int = _to_int_or_none(int_field)
        self.string_field: str = string_field
        self.datetime_field: dt.datetime = _to_date_time_or_none(
            datetime_field)
```

If there are types that need to be serialised in non-standard way, then check `_to_csv_safe_dict` in [csv_gen.py](./src/csv_gen.py). `_to_csv_safe_dict` is responsible for to string serialisation and can be modified to fit your needs.

### Writing to CSV
```py
import src.csv_gen as csv_gen


data = [
    Model(int_field=1, string_field="1", datetime_field=utc_now),
    Model(int_field=2, string_field="2", datetime_field=utc_now_plus_1)
]

csv_gen.write_as_csv(file_path, data)
```

### Reading from CSV

```py
import src.csv_gen as csv_gen


data: List[Model] = csv_gen.read_from_csv(path, Model)
```

## How to run tests

```sh
python3 -m pytest tests
```
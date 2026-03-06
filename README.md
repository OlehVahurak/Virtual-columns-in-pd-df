# Virtual-columns-in-pd-df

This project implements the `add_virtual_column` function for pandas DataFrames.

## Function Description

The `add_virtual_column` function adds a new column to a pandas DataFrame based on a mathematical expression.

### Parameters
- `df`: A pandas DataFrame.
- `role`: A string representing a mathematical expression (e.g., "quantity * price").
- `new_column`: The name of the new column to add.

### Validations
- All column names must consist only of letters and underscores.
- Supports operations: +, -, *.
- Raises ValueError if validations fail or expression cannot be evaluated.

### Usage
```python
import pandas as pd
from virtual_columns import add_virtual_column

df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
result = add_virtual_column(df, "a + b", "sum")
print(result)
```

### Exceptions
- `ValueError`: Raised for invalid column names, invalid new column name, or evaluation errors.

## Running Tests

To run tests with pytest:
```bash
pip install pytest
pytest -v test_unit.py
```
or 

```bash
pytest -v test_virtual_columns.py
```

The practical operation of the function can be checked by running the `run_example.py` script.
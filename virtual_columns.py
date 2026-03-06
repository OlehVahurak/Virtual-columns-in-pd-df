import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    """
    Adds a virtual column to a pandas DataFrame based on a mathematical expression.

    Parameters:
        df (pd.DataFrame): Original DataFrame.
        role (str): Mathematical expression using existing column names.
                    Supports +, -, *. Column names must contain only letters and underscores.
        new_column (str): Name of the new column to add.
                          Must contain only letters and underscores.

    Returns:
        pd.DataFrame: A new DataFrame with the added virtual column, or an empty DataFrame if validation fails.
    """
    # Regex for validating column names (only letters and underscores)
    valid_name_pattern = re.compile(r'^[a-zA-Z_]+$')

    # Validate existing column names
    invalid_cols = [col for col in df.columns if not valid_name_pattern.match(col)]
    if invalid_cols:
        return pd.DataFrame()
    
    # Validate new column name
    if not valid_name_pattern.match(new_column):
        return pd.DataFrame()
    
    # Create a copy and add the new column
    new_df = df.copy()
    try:
        new_df[new_column] = new_df.eval(role)
    except Exception:
        return pd.DataFrame()
    
    return new_df
    
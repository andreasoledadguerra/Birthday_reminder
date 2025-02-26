import pandas as pd
from pathlib import Path

def add_row(df:pd.DataFrame, row: list) -> pd.DataFrame:
    """Add a new row to the calendar" dataframe"""

    df_new_row = pd.DataFrame([row], columns=df.columns)
    return pd.concat([df, df_new_row], ignore_index=True)
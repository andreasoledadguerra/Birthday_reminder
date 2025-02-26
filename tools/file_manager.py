import pandas as pd
from pathlib import Path

def create_empty_df() -> pd.DataFrame:
    """Create an empty dataframe with the proper columns"""
    columns = ["name", "birthday", "gift"]
    return pd.Dataframe(columns=columns)

def initialize_calendar(path_calendar: Path) -> pd.DataFrame:
    """Initialize or load the calendar file"""
    if not path_calendar.exists():
        df = create_empty_df()
        df.to_csv(path_calendar)
        return df
    else:
        return pd.read_csv(path_calendar, index_col=0)
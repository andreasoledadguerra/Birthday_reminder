import pandas as pd
from pathlib import Path

def create_empty_df() -> pd.DataFrame:
    """Create an empty dataframe with the proper columns"""
    columns = ["name", "birthday", "gift"]
    return pd.DataFrame(columns=columns)

def initialize_calendar(path_calendar: Path) -> pd.DataFrame:
    """Initialize or load the calendar file"""
    if not path_calendar.exists():
        df = create_empty_df()
        df.to_csv(path_calendar)
        return df
    else:
        return pd.read_csv(path_calendar, index_col=0)

def edit_calendar(df: pd.DataFrame, path_calendar:Path) -> pd.DataFrame:
    #requesting data from the user
    col = ["name", "birthday", "gift"]
    record_id = input("Enter the column to modify: 'name', 'birthday', 'gift' ")
    new_data = input("Enter the new data")
    #modifying the value
    if col in df.columns:
        
        if record_id in df["ID"].values:
            df.loc[df["ID"] ==  record_id, col] = new_data
            print("Modification successful")
        else:
            print("Column not found")
    return df

def clear_calendar(df:pd.DataFrame, path_calendar:Path) -> pd.DataFrame:
    """Remove all rows while preserving the Dataframe structure"""
    return df.drop(df.index)

def save_calendar(df:pd.DataFrame, path_calendar:Path) -> None:
    """ Save the dataframe to the calendar file"""
    return df.to_csv(path_calendar)
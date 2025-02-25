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

def edit_calendar(df: pd.DataFrame, path_calendar:Path) -> pd.DataFrame:
#requesting data from the user
    id_row = int(input("\Set the row ID to modify"))
    column = input("Enter the column name to modify")
    new_value = input("Enter the new value")
    #modifying the value
    if column in df.columns and id_row in df["ID"].values:
        df.loc[df["ID"] == id_row, column] = new_value
        # Save modified file
        df.to_csv(path_calendar, index= False)
        print("Modification successful")
    else:
        ("ID or column not founded")
    return df

def save_calendar(df:pd.DataFrame, path_calendar:Path) -> None:
    """ Save the dataframe to the calendar file"""
    df.to_csv(path_calendar)
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
    """Edit or add new data on the calendar file"""
    is_choice_ok = False
    name = ""
    birthday = ""
    gift = ""
    while not is_choice_ok:
        #requesting data from the user
        choice = input("Elija una opción: 1. Agregar nombre \n 2. Agregar cumpleaños \n 3. Agregar regalo \n 4. Repetir opciones")
        choice = int(choice)
        if choice == 1:
            name = input(f"Please, enter de new name: ")
            is_choice_ok = True
                  
        elif choice == 2:
            birthday = input("Please, enter the new birthday (YYY-MM-DD): ")
            is_choice_ok = True
        elif choice == 3:
            gift = input("Please, enter the new gift: ")
            is_choice_ok = True
        else: 
             is_choice_ok == 4
             continue
    row = [name, birthday, gift]

def clear_calendar(df:pd.DataFrame, path_calendar:Path) -> pd.DataFrame:
    """Remove all rows while preserving the Dataframe structure"""
    return df.drop(df.index)

def save_calendar(df:pd.DataFrame, path_calendar:Path) -> None:
    """ Save the dataframe to the calendar file"""
    return df.to_csv(path_calendar)
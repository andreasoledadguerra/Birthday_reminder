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
    id = ""
    name = ""
    birthday = ""
    gift = ""
    while not is_choice_ok:
        #requesting data from the user
        choice = input("Choose row to edit.")
        choice = int(choice)
        print(df.to_string())
        is_choice_ok =True

        choice = input("Please, enter the ID you want to modify")
        choice = int(choice)
        is_choice_ok = True 
        
        choice = input("Choose the data you want to modify: 1. Name n\ 2. Birthday n\ 3. Gift n\ 4. Repeat options")
        choice = int(choice)
        is_choice_ok = True

        if choice == 1:
            name = input("Please, enter de new name: ")
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
    
    row = [id, name, birthday, gift]

    
    return pd.read_csv(path_calendar, index_col=0)
   
#def view_calendar(df:pd.DataFrame, path_calendar:Path) -> pd.DataFrame:  

def clear_calendar(df:pd.DataFrame, path_calendar:Path) -> pd.DataFrame:
    """Remove all rows while preserving the Dataframe structure"""
    return df.drop(df.index)


def save_calendar(df:pd.DataFrame, path_calendar:Path) -> None:
    """ Save the dataframe to the calendar file"""
    return df.to_csv(path_calendar)
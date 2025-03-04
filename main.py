import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
from tools.file_manager import initialize_calendar, edit_calendar, clear_calendar, save_calendar
from tools.calendar_manager import add_row

def main():
    """Main entry point for the birthday reminder application"""
    path_calendar = Path("calendar.csv")
    df = initialize_calendar(path_calendar)

    is_option_ok = False 
    while not is_option_ok: 
        option = input("Choose an option: 1. View file  \n 2. Edit \n 3. Delete all data")
        try:
            option = int(option)
        except Exception as e:
            print("Invalid value")

        if option == 1:
            is_option_ok = True
            print(df.to_string())

        elif option == 2:
            is_option_ok = True
            row = [id, name, birthday, gift]
            id = ""
            name = " "
            birthday = " "
            gift = "" 
            edit_calendar(df, path_calendar)
           
        elif option == 3:
            is_option_ok = True
            clear_calendar(df, path_calendar)
        else:
            is_option_ok = False

        df = add_row(df, row)

    save_calendar(df, path_calendar)

if __name__ == "__main__":
    main()


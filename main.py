import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
from tools.file_manager import initialize_calendar, edit_calendar, save_calendar

def main():
    """Main entry point for the birthday reminder application"""
    path_calendar = Path("calendar.csv")
    path_calendar.unlink(missing_ok=True)
    df = initialize_calendar(path_calendar)

    is_option_ok = False 
    while not is_option_ok: 
        option = input("Elija alguna opción: 1. Ver archivo  \n 2. Agregar cumpleaños \n 3. Editar \n 4. Borrar")
        try:
            option = int(option)
        except Exception as e:
            print("Valor inválido")

        if option == 1:
            is_option_ok =True
            pass

        elif option == 2:
            is_option_ok = True
            pass

        elif option == 3:
            is_option_ok = True
            edit_calendar(df, path_calendar)
            pass

        elif option == 4:
            is_option_ok = True
            pass
        else:
            is_option_ok = False


    save_calendar(df, path_calendar)

if __name__ == "__main__":
    main()

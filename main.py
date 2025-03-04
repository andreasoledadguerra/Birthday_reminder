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
        option = input("Elija alguna opción: 1. Ver archivo  \n 2. Agregar cumpleaños \n 3. Editar \n 4. Borrar")
        try:
            option = int(option)
        except Exception as e:
            print("Valor inválido")

        if option == 1:
            is_option_ok = True
            print(df.to_string())


        elif option == 2:
            is_option_ok = True
            
            
            is_choice_ok = False
            name = ""
            birthday = ""
            gift = ""

            while not is_choice_ok:
                choice = input("Elija una opción: 1. Editar nombre \n 2. Editar cumpleaños \n 3. Editar regalo \n 4. Repetir opciones")
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
            df = add_row(df, row)

        elif option == 3:
            is_option_ok = True
            edit_calendar(df, path_calendar)
           

        elif option == 4:
            is_option_ok = True
            clear_calendar(df, path_calendar)
        else:
            is_option_ok = False


    save_calendar(df, path_calendar)

if __name__ == "__main__":
    main()

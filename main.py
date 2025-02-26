import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
from tools.file_manager import initialize_calendar, edit_calendar, save_calendar

def main():
    """Main entry point for the birthday reminder application"""
    path_calendar = Path("calendar.csv")

    df = initialize_calendar(path_calendar)

    edit_calendar(df, path_calendar)

    save_calendar(df, path_calendar)

if __name__ == "__main__":
    main()



from pathlib import Path
from tools.file_manager import initialize_calendar, save_calendar

def main():
    """Main entry point for the birthday reminder application"""
    path_calendar = Path("calendar.csv")

    df = initialize_calendar(path_calendar)

    save_calendar(df, path_calendar)

if __name__ == "__main__":
    main()
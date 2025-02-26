import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta


def add_row(df:pd.DataFrame, row: list) -> pd.DataFrame:
    """Add a new row to the calendar" dataframe"""

    df_new_row = pd.DataFrame([row], columns=df.columns)
    return pd.concat([df, df_new_row], ignore_index=True)

def birthday_reminder(path_calendar: Path = None, days: int = 30) -> pd.DataFrame:
    """ Get birthdays that are coming up within the specified number of days"""
    # Get today's date
    today = datetime.now().date()

    # End date for our range
    end_date = today + timedelta(days=days)

    def days_until_next_birthday(birthday_str):
        try:
            birthday_date = datetime.strptime(birthday_str, "%Y-%m-%d").date()

            this_year_bday = datetime(today.year, birthday_date.month, birthday_date.day).date()

            if this_year_bday < today:
                this_year_bday = datetime(today.year + 1, birthday_date.month, birthday_date.day).date()

            days_until =(this_year_bday - today).days

            return days_until
        except ValueError:
            return float('inf')
        
    # Apply function to create a new column with days until next birthday
    df_with_days = df_with_days.copy()
    df_with_days['days_until_birthday'] = df_with_days['Birthday'].apply(days_until_next_birthday)
    
    # Filter to only include birthdays within our range
    upcoming_df = df_with_days[df_with_days['days_until_birthday'] <= days]
    
    # Sort by days until birthday (closest first)
    upcoming_df = upcoming_df.sort_values('days_until_birthday')
    
    # Remove the temporary column before returning
    return upcoming_df.drop(columns=['days_until_birthday'])
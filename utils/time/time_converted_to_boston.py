import pandas as pd
import pytz
from datetime import datetime

# Define the Boston timezone
boston_tz = pytz.timezone('America/New_York')

# Function to convert timezones
def convert_to_boston_time(time, timezone):
    if pd.isna(time) or pd.isna(timezone):
        print(f"Skipping conversion: time = {time}, timezone = {timezone}")
        return None
    try:
        # Get the local timezone from the TIMEZONE column
        local_tz = pytz.timezone(timezone)

        if time.tzinfo is None:  # Naive datetime
            # Localize the naive datetime to the provided timezone
            localized_time = local_tz.localize(time)
        else:  # Aware datetime
            # Convert directly to the local timezone
            localized_time = time.astimezone(local_tz)

        # Convert to Boston time
        boston_time = localized_time.astimezone(boston_tz)
        return boston_time.strftime('%Y-%m-%d %H:%M:%S')  # Return as naive datetime string
    except pytz.UnknownTimeZoneError:
        print(f"Unknown timezone: {timezone}")
        return None
    except Exception as e:
        print(f"Error processing time = {time} with timezone = {timezone}: {e}")
        return None

def convert_time_of_dataframe(df):
    # Convert columns to datetime if not already
    df['EVENT_START'] = pd.to_datetime(df['EVENT_START'], errors='coerce')
    df['EVENT_END'] = pd.to_datetime(df['EVENT_END'], errors='coerce')
    df['PREDICTED_END'] = pd.to_datetime(df['PREDICTED_END'], errors='coerce')

    # Log NaN counts before conversion
    print(f"Before conversion: NaN values in EVENT_START: {df['EVENT_START'].isna().sum()}")
    print(f"Before conversion: NaN values in TIMEZONE: {df['TIMEZONE'].isna().sum()}")

    # Apply the conversion function to all relevant columns
    df['EVENT_START_BOSTON'] = df.apply(
        lambda row: convert_to_boston_time(row['EVENT_START'], row['TIMEZONE']), axis=1
    )
    df['EVENT_END_BOSTON'] = df.apply(
        lambda row: convert_to_boston_time(row['EVENT_END'], row['TIMEZONE']), axis=1
    )
    df['PREDICTED_END_BOSTON'] = df.apply(
        lambda row: convert_to_boston_time(row['PREDICTED_END'], row['TIMEZONE']), axis=1
    )
    
    # Convert the new columns to datetime
    df['EVENT_START_BOSTON'] = pd.to_datetime(df['EVENT_START_BOSTON'], errors='coerce')
    df['EVENT_END_BOSTON'] = pd.to_datetime(df['EVENT_END_BOSTON'], errors='coerce')
    df['PREDICTED_END_BOSTON'] = pd.to_datetime(df['PREDICTED_END_BOSTON'], errors='coerce')
    
    # Add a new column for the new timezone
    df['NEW_TIMEZONE'] = 'America/New_York'

    # Log NaN counts after conversion
    print(f"After conversion: NaN values in EVENT_START_BOSTON: {df['EVENT_START_BOSTON'].isna().sum()}")
    print(f"After conversion: NaN values in EVENT_END_BOSTON: {df['EVENT_END_BOSTON'].isna().sum()}")
    print(f"After conversion: NaN values in PREDICTED_END_BOSTON: {df['PREDICTED_END_BOSTON'].isna().sum()}")

    # Check the first few rows to verify results
    print(df[['EVENT_START_BOSTON', 'EVENT_END_BOSTON', 'PREDICTED_END_BOSTON', 'NEW_TIMEZONE']].head())
    
    return df

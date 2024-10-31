import pandas as pd


def convert_to_datetime(df):
    # List of columns to convert to datetime format
    datetime_columns = ['CREATE_DT', 'UPDATE_DT', 'EVENT_START', 'EVENT_END', 'PREDICTED_END', 'ROW_INSERTED_DT', 'ROW_UPDATED_DT']

    # Convert the specified columns to datetime format
    df[datetime_columns] = df[datetime_columns].apply(pd.to_datetime, errors='coerce')

    return df
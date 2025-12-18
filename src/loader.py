"""
loader.py

This module handles data ingestion and basic validation.
It is responsible for reading the input CSV file, parsing dates,
sorting records, and ensuring required columns are present.
"""

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load stock price data from a CSV file and perform basic validation.

    Steps performed:
    - Reads the CSV file into a Pandas DataFrame
    - Converts the 'date' column to datetime
    - Sorts data by ticker and date
    - Validates presence of required columns

    Parameters
    ----------
    file_path : str
        Path to the input CSV file.

    Returns
    -------
    pd.DataFrame
        Cleaned and validated DataFrame ready for time-series processing.

    Raises
    ------
    ValueError
        If required columns are missing from the input file.
    """
    df = pd.read_csv(file_path)

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(["ticker", "date"])

    required_columns = {
        "date", "open", "high", "low", "close", "volume", "ticker"
    }
    if not required_columns.issubset(df.columns):
        raise ValueError("Input CSV does not contain required columns")

    return df

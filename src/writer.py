"""
writer.py

This module handles persistence logic by writing
per-ticker result files to disk.
"""

import os
import pandas as pd


def write_result(df: pd.DataFrame, ticker: str, output_dir: str):
    """
    Write the processed monthly data for a single ticker to a CSV file.

    The output file follows the naming convention:
    result_<TICKER>.csv

    Parameters
    ----------
    df : pd.DataFrame
        Final processed DataFrame for a single ticker.
    ticker : str
        Stock ticker symbol.
    output_dir : str
        Directory where output CSV files will be written.
    """
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"result_{ticker}.csv")

    df.to_csv(file_path, index=False)

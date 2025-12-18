"""
transformer.py

This module contains logic to transform daily stock price data
into monthly aggregates using financially correct OHLC rules.
"""

import pandas as pd


def monthly_aggregation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Resample daily stock data into monthly OHLC aggregates.

    Aggregation logic:
    - Open  : first trading day of the month
    - High  : maximum price within the month
    - Low   : minimum price within the month
    - Close : last trading day of the month
    - Volume: sum of daily volumes in the month

    Parameters
    ----------
    df : pd.DataFrame
        Daily stock price data for a single ticker.

    Returns
    -------
    pd.DataFrame
        Monthly aggregated DataFrame with OHLC values.
    """
    df = df.set_index("date")

    monthly_df = df.resample("ME").agg({
        "open": "first",
        "high": "max",
        "low": "min",
        "close": "last",
        "volume": "sum"
    })

    monthly_df = monthly_df.reset_index()
    return monthly_df

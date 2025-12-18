"""
indicators.py

This module computes technical indicators (SMA and EMA)
based on monthly closing prices using vectorized Pandas operations.
"""

import pandas as pd


def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add technical indicators to a monthly stock price DataFrame.

    Indicators calculated:
    - SMA_10 : 10-period Simple Moving Average
    - SMA_20 : 20-period Simple Moving Average
    - EMA_10 : 10-period Exponential Moving Average
    - EMA_20 : 20-period Exponential Moving Average

    All indicators are calculated using monthly closing prices.

    Parameters
    ----------
    df : pd.DataFrame
        Monthly aggregated stock price data containing a 'close' column.

    Returns
    -------
    pd.DataFrame
        DataFrame enriched with SMA and EMA indicator columns.
    """
    df = df.copy()

    df["SMA_10"] = df["close"].rolling(window=10).mean()
    df["SMA_20"] = df["close"].rolling(window=20).mean()

    df["EMA_10"] = df["close"].ewm(span=10, adjust=False).mean()
    df["EMA_20"] = df["close"].ewm(span=20, adjust=False).mean()

    return df

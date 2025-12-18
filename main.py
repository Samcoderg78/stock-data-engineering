"""
main.py

This script orchestrates the end-to-end data pipeline:
- Loads daily stock data
- Performs monthly aggregation
- Computes technical indicators
- Writes per-ticker output files
"""

from src.loader import load_data
from src.transformer import monthly_aggregation
from src.indicators import add_technical_indicators
from src.writer import write_result


INPUT_FILE = "data/output_file.csv"
OUTPUT_DIR = "output"


def main():
    """
    Execute the data engineering pipeline.

    Steps:
    1. Load and validate input data
    2. Process each ticker independently
    3. Aggregate daily data to monthly frequency
    4. Compute technical indicators
    5. Validate output size
    6. Write results to CSV files
    """
    df = load_data(INPUT_FILE)

    tickers = df["ticker"].unique()

    for ticker in tickers:
        ticker_df = df[df["ticker"] == ticker]

        monthly_df = monthly_aggregation(ticker_df)
        final_df = add_technical_indicators(monthly_df)

        if len(final_df) != 24:
            raise ValueError(f"{ticker} does not contain exactly 24 monthly records")

        write_result(final_df, ticker, OUTPUT_DIR)
    print("Data processing complete.")

if __name__ == "__main__":
    main()

## Overview
This project implements a data engineering pipeline to transform daily stock price data into monthly aggregated datasets and compute commonly used technical indicators. The objective is to provide a macro-level view of financial data by resampling daily prices, calculating moving averages, and partitioning the results per stock symbol.

The solution is implemented using Python and Pandas only, following vectorized operations and a modular code structure.

---

## Dataset
- Source: https://github.com/sandeep-tt/tt-intern-dataset  
- Duration: 2 years of daily stock price data  
- Stock Symbols:
```

AAPL, AMD, AMZN, AVGO, CSCO, MSFT, NFLX, PEP, TMUS, TSLA

```

### Input Schema
```

date, volume, open, high, low, close, adjclose, ticker

````

---

## Approach
The problem is treated as a small ETL-style data pipeline consisting of the following steps:

1. **Data Ingestion**
   - Load the CSV file using Pandas
   - Parse the `date` column as datetime
   - Sort records by `ticker` and `date`
   - Validate the presence of required columns

2. **Monthly Aggregation**
   Daily stock prices are resampled to monthly frequency using financially correct OHLC logic:
   - Open: first trading day of the month
   - Close: last trading day of the month
   - High: maximum price during the month
   - Low: minimum price during the month
   - Volume: sum of daily volumes

3. **Technical Indicators**
   Technical indicators are calculated after monthly aggregation using monthly closing prices:
   - Simple Moving Average (SMA 10, SMA 20)
   - Exponential Moving Average (EMA 10, EMA 20)

4. **Data Partitioning**
   - Each stock ticker is processed independently
   - One CSV file is generated per ticker following the naming convention:
     ```
     result_<TICKER>.csv
     ```

---

## Project Structure
````

stock-data-engineering/
├── data/
│   └── stock_prices.csv
├── src/
│   ├── loader.py
│   ├── transformer.py
│   ├── indicators.py
│   ├── writer.py
├── output/
│   └── result_AAPL.csv
├── main.py
├── requirements.txt
└── README.md

````

---

## Technical Decisions and Rationale
- Monthly resampling is performed before calculating indicators to ensure that SMA and EMA reflect long-term trends rather than daily noise.
- SMA values are unavailable for initial months due to insufficient historical data, which is expected behavior.
- EMA values are available from the first month since EMA uses a recursive calculation and can be initialized from the first available closing price.
- Pandas `resample`, `rolling`, and `ewm` functions are used to ensure vectorized and efficient computations without relying on third-party technical analysis libraries.

---

## Assumptions
- The input dataset contains valid and continuous daily trading records.
- Each stock ticker spans exactly 24 months.
- Missing SMA values in initial rows are acceptable and mathematically correct.
- The dataset does not contain missing or corrupt critical values.

---

## How to Run

### Prerequisites
- Python 3.8 or higher
- Pandas

### Installation
```bash
pip install -r requirements.txt
````

### Execution

```bash
python main.py
```

---

## Output

* The pipeline generates 10 CSV files under the `output/` directory.
* Each file contains exactly 24 rows, representing monthly data for one stock ticker.
* Output files include monthly OHLC values along with SMA and EMA indicators.

---

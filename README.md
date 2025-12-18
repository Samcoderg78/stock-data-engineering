```md
# Data Engineering Intern Hiring Assignment

## Overview
This project demonstrates a data engineering pipeline that transforms **daily stock price data** into **monthly aggregated datasets** and computes key **technical indicators** used in financial analysis.

The solution focuses on:
- Correct financial aggregation logic (OHLC)
- Vectorized time-series processing using Pandas
- Clean, modular, and production-style code structure

The final output consists of **one CSV file per stock ticker**, each containing **24 monthly records** with calculated indicators.

---

## Dataset
- **Source:** https://github.com/sandeep-tt/tt-intern-dataset
- **Duration:** 2 years of daily stock price data
- **Tickers:**  
  `AAPL, AMD, AMZN, AVGO, CSCO, MSFT, NFLX, PEP, TMUS, TSLA`

### Input Schema
```

date, volume, open, high, low, close, adjclose, ticker

```

---

## Solution Approach

The problem is implemented as a small **ETL-style data pipeline**:

### 1. Extract
- Load the raw CSV file
- Parse dates and validate schema
- Sort data by ticker and date to ensure time-series correctness

### 2. Transform (Monthly Aggregation)
Daily stock prices are resampled to **monthly frequency** using financially correct OHLC rules:

| Field | Monthly Logic |
|------|---------------|
| Open | First trading day of the month |
| Close | Last trading day of the month |
| High | Maximum price during the month |
| Low | Minimum price during the month |
| Volume | Sum of daily volumes |

### 3. Enrich (Technical Indicators)
Technical indicators are calculated **after monthly aggregation**, based on **monthly closing prices**:
- SMA 10
- SMA 20
- EMA 10
- EMA 20

### 4. Partition & Persist
- Data is processed **independently per ticker**
- One output CSV is generated per ticker following the naming convention:
```

result_<TICKER>.csv

```

---

## Project Structure

```

stock-data-engineering/
│
├── data/
│   └── stock_prices.csv
│
├── src/
│   ├── loader.py        # Data loading & validation
│   ├── transformer.py  # Monthly OHLC aggregation
│   ├── indicators.py   # SMA & EMA calculations
│   ├── writer.py       # Output file generation
│
├── output/
│   └── result_AAPL.csv
│
├── main.py              # Pipeline orchestration
├── requirements.txt
└── README.md

````

---

## Technical Decisions & Rationale

### Why resample before calculating indicators?
Technical indicators must reflect **monthly trends**, not daily fluctuations.  
Indicators are therefore calculated on **monthly closing prices**, after resampling.

### Why SMA has missing values initially?
Simple Moving Averages require a full window (10 or 20 months).  
Missing values (`NaN`) for early months are **expected and correct**.

### Why EMA appears earlier than SMA?
EMA uses a recursive formula and can be initialized from the first available value, allowing it to be computed immediately.

### Why Pandas only?
The assignment constraints require:
- Vectorized operations
- No third-party technical analysis libraries  
Pandas’ `resample`, `rolling`, and `ewm` functions satisfy these requirements efficiently.

---

## Assumptions
- Input data contains valid daily trading records
- Each ticker has continuous data covering exactly 24 months
- Missing SMA values for initial months are acceptable
- No missing or corrupt rows in the input dataset

---

## How to Run

### Prerequisites
- Python 3.8+
- Pandas

### Install Dependencies
```bash
pip install -r requirements.txt
````

### Execute Pipeline

```bash
python main.py
```

---

## Output

* **10 CSV files** generated under the `output/` directory
* Each file:

  * Represents one stock ticker
  * Contains exactly **24 monthly records**
  * Includes OHLC values and SMA/EMA indicators

---

## Evaluation Alignment

This solution explicitly addresses:

* ✔ Correct OHLC aggregation
* ✔ Accurate SMA & EMA calculations
* ✔ Efficient per-ticker partitioning
* ✔ Vectorized Pandas operations
* ✔ Clean, modular code structure

```

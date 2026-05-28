# NSE Stock Market Analytics & Risk Intelligence Dashboard

An end-to-end automated financial data pipeline and interactive dashboard analyzing 9 major NSE-listed Indian stocks from 2020-2025.

## Project Overview

This project simulates a real-world financial analytics workflow — from raw data extraction to automated anomaly detection to interactive executive reporting.

## Tech Stack

- **Python** — Data extraction, transformation, validation
- **SQL (SQLite)** — Data storage and querying
- **Power BI** — Interactive 2-page dashboard
- **yfinance** — Real-time NSE stock data via Yahoo Finance
- **Pandas** — Data cleaning and feature engineering
- **Gemini API** — LLM-powered financial summary generation

## Pipeline Architecture

```text
Yahoo Finance API
        ↓
extract.py — Fetch 5-year NSE stock data
        ↓
transform.py — Clean, validate, detect anomalies
        ↓
load.py — Store in SQLite database (3 tables)
        ↓
llm_summary.py — Gemini API generates plain English report
        ↓
Power BI Dashboard — 2-page interactive visualization
```

## Dataset

- **9 Companies:** RELIANCE, TCS, HDFCBANK, INFY, MARUTI, ADANIENT, BAJFINANCE, WIPRO, SUNPHARMA
- **Time Period:** January 2020 — December 2025
- **Total Records:** 7,000+ daily stock records
- **Source:** Yahoo Finance (via yfinance library)

## Key Features

### ETL Pipeline

- Automated data extraction from Yahoo Finance API
- Data type validation and null checks
- Feature engineering — Daily Return % calculation
- Anomaly detection — flags moves greater than 3% in single day
- Monthly aggregation summaries

### Database (SQLite — 3 Tables)

- `stock_prices` — All cleaned daily records
- `monthly_summary` — Aggregated monthly metrics
- `anomalies` — Flagged high-impact market events

### Power BI Dashboard

#### Page 1 — Overview & Trends

- KPI Cards: Total Stocks, Volume, Anomalies, Highest Gain, Biggest Drop
- NSE Stock Price Trends 2020-2025 (Line Chart)
- Monthly Average Closing Price (Bar Chart)
- Total Volume Distribution by Ticker (Donut Chart)
- Top 5 Gainers and Top 5 Losers

#### Page 2 — Analytics & Risk Insights

- Anomalies Over Time (Area Chart)
- Top Anomalies Table with conditional formatting
- Volatility Ranking by Company (Std Dev of Daily Returns)
- Daily Return Distribution (Bell Curve)
- Top 5 Most Traded Stocks

## Key Findings

- **1,128 anomalies** detected across 5-year period
- **ADANIENT.NS** most volatile stock (Std Dev: 3.2%)
- **Biggest single-day crash:** ADANIENT.NS -28.20% (Feb 2023)
- **Biggest single-day gain:** ADANIENT.NS +23.66%
- **COVID-19 impact:** 400+ anomalies in 2020 alone
- **Most traded:** HDFCBANK.NS (38bn shares)
- **Best performer:** SUNPHARMA.NS (highest overall growth)

## How to Run

### Prerequisites

```bash
pip install yfinance pandas sqlalchemy google-genai openpyxl
```

### Run Pipeline

```bash
python extract.py      # Fetch stock data
python transform.py    # Clean and detect anomalies
python load.py         # Load into SQLite
python llm_summary.py  # Generate AI summary (requires Gemini API key)
```

### View Dashboard

Open `NSE_Stock_Dashboard.pbix` in Power BI Desktop.

## Project Structure

```text
nse-stock-analytics/
├── extract.py               # Data extraction
├── transform.py             # ETL + anomaly detection
├── load.py                  # SQLite loading
├── llm_summary.py           # Gemini API integration
├── finance.db               # SQLite database
├── raw_stock_data.csv       # Raw extracted data
├── cleaned_stock_data.csv   # Processed data
├── monthly_summary.csv      # Monthly aggregations
├── anomalies.csv            # Detected anomalies
└── NSE_Stock_Dashboard.pbix # Power BI dashboard
```

## Skills Demonstrated

- ETL Pipeline Development
- Financial Data Analysis
- Anomaly Detection
- SQL Database Management
- LLM API Integration (Gemini)
- Data Visualization (Power BI)
- Automated Reporting
- SDLC Documentation

## Author

**Anjali Dogra**  
B.Sc. Data Science — IIT Madras

**LinkedIn:** https://linkedin.com/in/anjali-dogra  
**GitHub:** https://github.com/anjalidogra01

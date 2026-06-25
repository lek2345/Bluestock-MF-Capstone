# Mutual Fund Analytics Dashboard

## Project Overview

The Mutual Fund Analytics Dashboard is an end-to-end data analytics project developed to analyze mutual fund performance, investor behavior, SIP trends, portfolio risk, and industry growth. The project uses Python for ETL, data cleaning, exploratory analysis, performance analytics, and Power BI for interactive dashboard visualization.

---

## Problem Statement

Mutual fund investors, analysts, and financial institutions require a centralized platform to evaluate fund performance, monitor investment trends, assess portfolio risk, and derive actionable insights from large volumes of financial data.

This project provides a comprehensive analytics solution using historical mutual fund data, investor transaction data, and market benchmarks.

---

## Objectives

* Perform end-to-end ETL and data cleaning.
* Analyze mutual fund performance using financial metrics.
* Study investor behavior and SIP trends.
* Build interactive dashboards for business insights.
* Implement advanced risk analytics and fund recommendations.
* Generate actionable insights for investors and analysts.

---

## Dataset Description

The project uses the following datasets:

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category-wise Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## Project Workflow

### 1. Data Ingestion

* Loaded all datasets using Pandas.
* Validated dataset structure and integrity.
* Performed AMFI Code validation.
* Fetched live NAV data using MFAPI.

### 2. Data Cleaning

* Removed duplicates.
* Handled missing values.
* Standardized date formats.
* Validated transaction records.
* Cleaned NAV and performance datasets.

### 3. Database Creation

* Designed SQLite database schema.
* Created dimension and fact tables.
* Loaded cleaned datasets into SQLite.
* Executed analytical SQL queries.

### 4. Exploratory Data Analysis (EDA)

* NAV Trend Analysis
* AUM Growth Analysis
* SIP Trend Analysis
* Folio Growth Analysis
* Category Inflow Analysis
* Investor Demographics Analysis
* Geographic Distribution Analysis
* Correlation Analysis

### 5. Performance Analytics

Calculated key financial metrics:

* Daily Returns
* CAGR (Compound Annual Growth Rate)
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Fund Scorecard Ranking

### 6. Advanced Analytics

* Historical Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation Model
* Sector Concentration Analysis (HHI)

### 7. Dashboard Development

Developed interactive Power BI dashboards:

#### Executive Summary

* Total AUM
* Total SIP Inflows
* Total Folios
* Total Schemes
* AUM Growth Trends

#### Investor Analytics

* Age Group Distribution
* Gender Distribution
* Transaction Type Analysis
* Payment Mode Analysis
* State-wise Investments

#### Fund Performance

* Top Funds by CAGR
* Top Funds by Sharpe Ratio
* Top Funds by Sortino Ratio
* Maximum Drawdown Analysis

#### SIP & Market Trends

* SIP Growth Trends
* Category-wise Inflows
* Market Performance Analysis

---

## Technologies Used

### Programming & Analytics

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly

### Database

* SQLite
* SQLAlchemy

### Visualization

* Power BI

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

### APIs

* MFAPI (mfapi.in)

---

## Installation & Setup

### Clone Repository

```bash
git clone <repository-url>
cd Bluestock-MF-Capstone
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Data Ingestion

```bash
python scripts/data_ingestion.py
```

### Run Data Cleaning

```bash
python scripts/data_cleaning.py
```

### Create Database

```bash
python scripts/create_database.py
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

### Open Power BI Dashboard

Open the Power BI dashboard file from the dashboard folder.

---

## Project Structure

```text
Bluestock-MF-Capstone/

data/
├── raw/
├── processed/

database/
├── bluestock_mf.db

notebooks/
├── 03_eda_analysis.ipynb
├── 04_performance_analytics.ipynb
├── 05_advanced_analytics.ipynb
├── AMFI_Validation.ipynb

scripts/
├── data_ingestion.py
├── data_cleaning.py
├── create_database.py
├── live_nav_fetch.py
├── recommender.py

sql/
├── schema.sql
├── queries.sql

dashboard/
├── Bluestock_Mutual_Fund_Dashboard.pbix

reports/

Screenshots/

README.md
requirements.txt
```

---

## Key Insights

* Identified top-performing mutual funds using risk-adjusted return metrics.
* Evaluated portfolio risk using VaR, CVaR, and Maximum Drawdown.
* Analyzed investor demographics and transaction behavior.
* Studied SIP growth trends and mutual fund industry expansion.
* Built a recommendation model based on investor risk appetite.
* Measured portfolio concentration using the Herfindahl-Hirschman Index (HHI).

---

## Future Enhancements

* Streamlit Web Dashboard
* Automated Daily NAV Updates
* Portfolio Optimization Module
* Monte Carlo Simulation for NAV Forecasting
* Automated Report Generation

---

## Author

**Lekha Reddy D**
MSc Computer Science (Data Science)

---

## License

This project was developed as part of the Bluestock Fintech Mutual Fund Analytics Capstone Project for educational and learning purposes.

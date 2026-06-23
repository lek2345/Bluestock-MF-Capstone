# Mutual Fund Analytics Dashboard

## Project Overview

The Mutual Fund Analytics Dashboard is an end-to-end data analytics project designed to analyze mutual fund performance, investor behavior, SIP trends, and industry growth. The project uses Python for data processing and Power BI for interactive dashboard visualization.

## Problem Statement

Mutual fund investors and analysts require a centralized platform to evaluate fund performance, track investment trends, and identify key insights from large volumes of financial data. This project aims to provide data-driven insights through analytical metrics and dashboards.

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

## Project Workflow

### 1. Data Ingestion

* Loaded and validated all datasets using Pandas.
* Performed AMFI code validation.
* Fetched live NAV data using MFAPI.

### 2. Data Cleaning

* Handled missing values.
* Standardized column formats.
* Validated data consistency.

### 3. Exploratory Data Analysis (EDA)

* Fund house analysis
* SIP trend analysis
* AUM analysis
* Folio growth analysis
* Category inflow analysis

### 4. Performance Analytics

Calculated key financial metrics:

* CAGR (Compound Annual Growth Rate)
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown

### 5. Dashboard Development

Developed interactive Power BI dashboards:

#### Executive Summary

* Total SIP Inflows
* Total Folios
* Total Schemes
* AUM by Fund House
* SIP Trends
* Industry Folio Growth

#### Investor Analytics

* Age Group Distribution
* Gender Distribution
* Transaction Type Analysis
* Payment Mode Analysis

#### Fund Performance

* Top Funds by CAGR
* Top Funds by Sharpe Ratio
* Top Funds by Sortino Ratio
* Maximum Drawdown Analysis

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Requests
* Jupyter Notebook
* SQL
* Power BI
* Git
* GitHub

## Key Insights

* Identified top-performing mutual funds using risk-adjusted metrics.
* Analyzed investor demographics and transaction patterns.
* Evaluated SIP growth trends and industry expansion.
* Compared fund performance using multiple financial indicators.

## Project Structure

Bluestock-MF-Capstone/

* data/
* notebooks/
* scripts/
* sql/
* dashboard/
* reports/
* requirements.txt

## Author

Lekha Reddy
MSc Computer Science (Data Science)

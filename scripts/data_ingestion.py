import pandas as pd
import os

# Path to raw data
DATA_PATH = "data/raw"

# List of files
files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    path = os.path.join(DATA_PATH, file)
    df = pd.read_csv(path)

    print("=" * 60)
    print(file)
    print("Rows and Columns:", df.shape)
    print(df.head())
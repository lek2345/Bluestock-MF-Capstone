import pandas as pd
import sqlite3
import os

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

# Connect to SQLite database
conn = sqlite3.connect("database/bluestock_mf.db")

# Load datasets
fund_master = pd.read_csv(os.path.join(RAW_PATH, "01_fund_master.csv"))
nav = pd.read_csv(os.path.join(PROCESSED_PATH, "clean_nav_history.csv"))
transactions = pd.read_csv(os.path.join(PROCESSED_PATH, "clean_investor_transactions.csv"))
performance = pd.read_csv(os.path.join(RAW_PATH, "07_scheme_performance.csv"))
aum = pd.read_csv(os.path.join(RAW_PATH, "03_aum_by_fund_house.csv"))
sip = pd.read_csv(os.path.join(RAW_PATH, "04_monthly_sip_inflows.csv"))

# Save to SQLite
fund_master.to_sql("dim_fund", conn, if_exists="replace", index=False)
nav.to_sql("fact_nav", conn, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", conn, if_exists="replace", index=False)
performance.to_sql("fact_performance", conn, if_exists="replace", index=False)
aum.to_sql("fact_aum", conn, if_exists="replace", index=False)
sip.to_sql("fact_sip", conn, if_exists="replace", index=False)

conn.close()

print("✅ SQLite Database created successfully!")
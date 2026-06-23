import pandas as pd
import os

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

# Create processed folder if it doesn't exist
os.makedirs(PROCESSED_PATH, exist_ok=True)

# Load NAV History
nav = pd.read_csv(os.path.join(RAW_PATH, "02_nav_history.csv"))

# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"])

# Sort values
nav = nav.sort_values(by=["amfi_code", "date"])

# Remove duplicates
nav = nav.drop_duplicates()

# Forward fill missing NAV values
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Save cleaned file
nav.to_csv(
    os.path.join(PROCESSED_PATH, "clean_nav_history.csv"),
    index=False
)

print("✅ NAV History cleaned successfully!")

# Load Investor Transactions
transactions = pd.read_csv(
    os.path.join(RAW_PATH, "08_investor_transactions.csv")
)

# Standardize transaction types
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

# Remove invalid amounts
transactions = transactions[
    transactions["amount_inr"] > 0
]

# Save cleaned transactions
transactions.to_csv(
    os.path.join(PROCESSED_PATH, "clean_investor_transactions.csv"),
    index=False
)

print("✅ Investor Transactions cleaned successfully!")
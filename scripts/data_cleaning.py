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

# Load Scheme Performance
performance = pd.read_csv(
    os.path.join(RAW_PATH, "07_scheme_performance.csv")
)

# Convert return columns to numeric
cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "sharpe_ratio"
]

for col in cols:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )

# Flag negative Sharpe
performance["negative_sharpe"] = (
    performance["sharpe_ratio"] < 0
)

# Validate expense ratio
if "expense_ratio_pct" in performance.columns:
    performance["expense_ratio_valid"] = (
        (performance["expense_ratio_pct"] >= 0.1)
        &
        (performance["expense_ratio_pct"] <= 2.5)
    )

# Remove duplicates
performance = performance.drop_duplicates()

# Save
performance.to_csv(
    os.path.join(
        PROCESSED_PATH,
        "clean_scheme_performance.csv"
    ),
    index=False
)

print("✅ Scheme Performance cleaned successfully!")
# Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|----------|-------------|
| amfi_code | TEXT | Unique AMFI scheme code |
| fund_house | TEXT | Mutual fund company |
| scheme_name | TEXT | Fund scheme name |
| category | TEXT | Equity, Debt, Hybrid |
| sub_category | TEXT | Large Cap, Mid Cap, etc. |
| plan | TEXT | Direct or Regular |

## fact_nav

| Column | Type | Description |
|----------|----------|-------------|
| amfi_code | TEXT | Scheme code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

## fact_transactions

| Column | Type | Description |
|----------|----------|-------------|
| investor_id | TEXT | Investor identifier |
| transaction_date | DATE | Transaction date |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction amount |

## fact_performance

| Column | Type | Description |
|----------|----------|-------------|
| return_1yr_pct | REAL | 1 year return |
| return_3yr_pct | REAL | 3 year return |
| sharpe_ratio | REAL | Risk adjusted return |
| sortino_ratio | REAL | Downside risk metric |

## fact_aum

| Column | Type | Description |
|----------|----------|-------------|
| fund_house | TEXT | AMC name |
| aum_crore | REAL | Assets under management |

## fact_sip

| Column | Type | Description |
|----------|----------|-------------|
| month | TEXT | Month |
| sip_inflow_crore | REAL | SIP inflow amount |
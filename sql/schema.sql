CREATE TABLE dim_fund (
    amfi_code TEXT PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT
);

CREATE TABLE fact_nav (
    amfi_code TEXT,
    date DATE,
    nav REAL
);

CREATE TABLE fact_transactions (
    investor_id TEXT,
    transaction_date DATE,
    amfi_code TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT
);

CREATE TABLE fact_performance (
    amfi_code TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL
);

CREATE TABLE fact_aum (
    fund_house TEXT,
    aum_crore REAL
);

CREATE TABLE fact_sip (
    month TEXT,
    sip_inflow_crore REAL
);
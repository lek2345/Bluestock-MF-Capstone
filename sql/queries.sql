-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV for each fund
SELECT amfi_code, AVG(nav) AS average_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Number of transactions by type
SELECT transaction_type, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

-- 4. Total investment amount by state
SELECT state, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with expense ratio less than 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Count of funds by category
SELECT category, COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category;

-- 7. Average return by category
SELECT category,
AVG(return_1yr_pct) AS avg_return
FROM fact_performance
GROUP BY category;

-- 8. Top 10 investors by investment
SELECT investor_id,
SUM(amount_inr) AS invested_amount
FROM fact_transactions
GROUP BY investor_id
ORDER BY invested_amount DESC
LIMIT 10;

-- 9. Number of investors by gender
SELECT gender,
COUNT(*) AS total
FROM fact_transactions
GROUP BY gender;

-- 10. Average SIP amount by age group
SELECT age_group,
AVG(amount_inr) AS avg_sip
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY age_group;
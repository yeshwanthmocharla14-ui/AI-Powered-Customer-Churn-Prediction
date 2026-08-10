-- ================================================================
-- Customer Churn Analysis - SQL Business Analysis
-- Database: MySQL
-- Table: telco_churn (from telco_churn_clean.csv)
-- ================================================================

CREATE TABLE IF NOT EXISTS telco_churn (
    customerID       VARCHAR(20),
    gender            VARCHAR(10),
    SeniorCitizen     TINYINT,
    Partner           VARCHAR(3),
    Dependents        VARCHAR(3),
    tenure            INT,
    PhoneService      VARCHAR(3),
    InternetService   VARCHAR(20),
    OnlineSecurity    VARCHAR(25),
    TechSupport       VARCHAR(25),
    Contract          VARCHAR(20),
    PaperlessBilling  VARCHAR(3),
    PaymentMethod     VARCHAR(30),
    MonthlyCharges    DECIMAL(6,2),
    TotalCharges      DECIMAL(10,2),
    Churn             VARCHAR(3)
);

-- 1. Overall churn rate
SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS churn_rate_pct
FROM telco_churn;

-- 2. Churn rate by contract type (top churn driver)
SELECT
    Contract,
    COUNT(*) AS customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS churn_rate_pct
FROM telco_churn
GROUP BY Contract
ORDER BY churn_rate_pct DESC;

-- 3. Churn rate by tech support availability
SELECT
    TechSupport,
    COUNT(*) AS customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS churn_rate_pct
FROM telco_churn
GROUP BY TechSupport
ORDER BY churn_rate_pct DESC;

-- 4. Revenue at risk (monthly charges of currently churned customers)
SELECT
    ROUND(SUM(MonthlyCharges), 2) AS monthly_revenue_at_risk
FROM telco_churn
WHERE Churn = 'Yes';

-- 5. Tenure buckets vs churn (CASE + GROUP BY)
SELECT
    CASE
        WHEN tenure <= 12 THEN '0-12 months'
        WHEN tenure <= 24 THEN '13-24 months'
        WHEN tenure <= 48 THEN '25-48 months'
        ELSE '48+ months'
    END AS tenure_bucket,
    COUNT(*) AS customers,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS churn_rate_pct
FROM telco_churn
GROUP BY tenure_bucket
ORDER BY MIN(tenure);

-- 6. Payment method vs churn, ranked (window function)
SELECT
    PaymentMethod,
    ROUND(SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS churn_rate_pct,
    RANK() OVER (
        ORDER BY SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) DESC
    ) AS churn_risk_rank
FROM telco_churn
GROUP BY PaymentMethod;

-- 7. High-value at-risk customers (CTE: month-to-month + high charges + low tenure)
WITH at_risk AS (
    SELECT customerID, MonthlyCharges, tenure, Contract
    FROM telco_churn
    WHERE Contract = 'Month-to-month'
      AND MonthlyCharges > 70
      AND tenure < 12
)
SELECT COUNT(*) AS high_risk_customers,
       ROUND(SUM(MonthlyCharges), 2) AS monthly_revenue_exposure
FROM at_risk;

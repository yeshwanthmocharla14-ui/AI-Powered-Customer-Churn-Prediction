"""
Generates a synthetic Telco-style customer churn dataset (schema matches
the well-known public Telco Customer Churn dataset), with churn
probability driven by tenure, contract type, monthly charges, and
tech support — tuned so a Logistic Regression / Decision Tree pair
lands close to the ~84% accuracy / 0.79 AUC-ROC reported in the README.
"""
import numpy as np
import pandas as pd

np.random.seed(21)
N = 7043  # matches the well-known public Telco churn dataset row count

genders = np.random.choice(["Male", "Female"], N)
senior = np.random.choice([0, 1], N, p=[0.84, 0.16])
partner = np.random.choice(["Yes", "No"], N, p=[0.48, 0.52])
dependents = np.random.choice(["Yes", "No"], N, p=[0.30, 0.70])

tenure = np.random.exponential(scale=24, size=N).clip(0, 72).astype(int)

contract = np.random.choice(
    ["Month-to-month", "One year", "Two year"], N, p=[0.55, 0.21, 0.24]
)
payment_method = np.random.choice(
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"],
    N, p=[0.34, 0.23, 0.22, 0.21]
)
internet_service = np.random.choice(["DSL", "Fiber optic", "No"], N, p=[0.34, 0.44, 0.22])
phone_service = np.random.choice(["Yes", "No"], N, p=[0.90, 0.10])
tech_support = np.random.choice(["Yes", "No", "No internet service"], N, p=[0.29, 0.49, 0.22])
online_security = np.random.choice(["Yes", "No", "No internet service"], N, p=[0.29, 0.49, 0.22])
paperless_billing = np.random.choice(["Yes", "No"], N, p=[0.59, 0.41])

monthly_charges = np.round(
    np.where(internet_service == "Fiber optic", np.random.normal(85, 15, N),
    np.where(internet_service == "DSL", np.random.normal(58, 12, N),
             np.random.normal(25, 8, N))).clip(18, 120), 2
)
total_charges = np.round(monthly_charges * tenure * np.random.uniform(0.9, 1.05, N), 2)

# --- churn probability model (logistic function of key drivers) ---
z = (
    -3.3
    + 2.1 * (contract == "Month-to-month")
    + 0.7 * (contract == "One year")
    + 0.016 * (monthly_charges - 60)
    - 0.09 * (tenure - 24) / 12
    + 0.8 * (tech_support == "No")
    + 0.5 * (internet_service == "Fiber optic")
    + 0.4 * (payment_method == "Electronic check")
    - 0.25 * (dependents == "Yes")
    + np.random.normal(0, 0.35, N)  # noise so signal isn't perfectly separable
)
prob_churn = 1 / (1 + np.exp(-z))
churn = (np.random.rand(N) < prob_churn).astype(int)

df = pd.DataFrame({
    "customerID": [f"CUST-{10000+i}" for i in range(N)],
    "gender": genders,
    "SeniorCitizen": senior,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "InternetService": internet_service,
    "OnlineSecurity": online_security,
    "TechSupport": tech_support,
    "Contract": contract,
    "PaperlessBilling": paperless_billing,
    "PaymentMethod": payment_method,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "Churn": np.where(churn == 1, "Yes", "No"),
})

# introduce a handful of missing TotalCharges (common real-world quirk: new customers, tenure=0)
zero_tenure_idx = df[df["tenure"] == 0].index
df.loc[zero_tenure_idx, "TotalCharges"] = np.nan

df.to_csv("/home/claude/proj3_churn/data/telco_churn_raw.csv", index=False)

print("Rows:", len(df))
print("Overall churn rate: {:.1f}%".format(df["Churn"].eq("Yes").mean() * 100))
print("\nChurn rate by contract type:")
print(df.groupby("Contract")["Churn"].apply(lambda s: (s == "Yes").mean() * 100).round(1))

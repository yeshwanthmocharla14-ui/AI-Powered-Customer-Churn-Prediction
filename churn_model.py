import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, confusion_matrix

df = pd.read_csv("../data/telco_churn_raw.csv")
df["TotalCharges"] = df["TotalCharges"].fillna(df["MonthlyCharges"])
df = df.drop(columns=["customerID"])

target = (df["Churn"] == "Yes").astype(int)
X = df.drop(columns=["Churn"])

cat_cols = X.select_dtypes(include="object").columns
for c in cat_cols:
    X[c] = LabelEncoder().fit_transform(X[c])

X_train, X_test, y_train, y_test = train_test_split(
    X, target, test_size=0.2, random_state=42, stratify=target
)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train_s, y_train)
pred_lr = log_reg.predict(X_test_s)
proba_lr = log_reg.predict_proba(X_test_s)[:, 1]

print("=== Logistic Regression ===")
print("Accuracy:", round(accuracy_score(y_test, pred_lr), 3))
print("AUC-ROC :", round(roc_auc_score(y_test, proba_lr), 3))
print(classification_report(y_test, pred_lr))

tree = DecisionTreeClassifier(max_depth=6, min_samples_leaf=40, random_state=42)
tree.fit(X_train, y_train)
pred_dt = tree.predict(X_test)
proba_dt = tree.predict_proba(X_test)[:, 1]

print("\n=== Decision Tree ===")
print("Accuracy:", round(accuracy_score(y_test, pred_dt), 3))
print("AUC-ROC :", round(roc_auc_score(y_test, proba_dt), 3))

importances = pd.Series(tree.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nTop 5 churn drivers (Decision Tree feature importance):")
print(importances.head(5))

# 🤖 Customer Churn Prediction & Analytics Dashboard

## 📌 Project Overview

This project focuses on analyzing customer behavior and predicting customer churn using Machine Learning techniques. The objective is to identify the key factors influencing customer attrition and provide actionable business insights through an interactive Power BI dashboard.

The project covers the complete data analytics workflow including data cleaning, exploratory data analysis (EDA), feature engineering, machine learning model development, and dashboard creation.


## 🎯 Business Problem

Customer churn is one of the biggest challenges for subscription-based businesses. Losing existing customers directly impacts revenue and growth.

This project aims to:

- Identify customers who are likely to churn.
- Understand the major factors influencing churn.
- Measure revenue at risk due to customer attrition.
- Provide business recommendations to improve customer retention.


## 📊 Dataset Information

The dataset contains customer demographic information, account details, subscription information, and churn status.

### Key Features

- Customer Demographics
  - Gender
  - Senior Citizen
  - Partner
  - Dependents

- Service Information
  - Phone Service
  - Internet Service
  - Online Security
  - Online Backup
  - Device Protection
  - Tech Support
  - Streaming TV
  - Streaming Movies

- Account Information
  - Contract Type
  - Payment Method
  - Monthly Charges
  - Total Charges
  - Tenure

- Target Variable
  - Churn (Yes / No)


## 🛠️ Tools & Technologies Used

### 📊 Data Analysis
- SQL
- Python
- Pandas
- NumPy

### 📈 Data Visualization
- Matplotlib
- Seaborn
- Power BI

### 🤖 Machine Learning
- Scikit-learn
- Logistic Regression
- Decision Tree Classifier

### 💻 Development Environment
- VS Code
- Jupyter Notebook
- GitHub


## 🔍 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Customer Churn Distribution
- Gender vs Churn Analysis
- Contract Type vs Churn
- Internet Service vs Churn
- Monthly Charges Analysis
- Customer Tenure Analysis
- Payment Method Analysis

Key insights revealed significant churn among customers with:
- Month-to-Month contracts
- Higher monthly charges
- Short customer tenure
- Certain internet service categories


## ⚙️ Data Preprocessing

The following preprocessing steps were performed:

- Removed unnecessary columns
- Handled missing values
- Converted data types
- Encoded categorical variables
- Feature scaling using StandardScaler
- Train-Test Split


## 🤖 Machine Learning Models

### 1️⃣ Logistic Regression

Used for binary classification to predict customer churn.

Evaluation Metrics:

- Accuracy Score
- Confusion Matrix
- Classification Report


### 2️⃣ Decision Tree Classifier

Used to identify the most important features influencing customer churn.

Evaluation Metrics:

- Accuracy Score
- Feature Importance Analysis
- Classification Report


## 📈 Power BI Dashboard

An interactive dashboard was created to visualize customer churn patterns and business insights.

### Dashboard Features

✅ Total Customers KPI

✅ Churn Customers KPI

✅ Churn Rate KPI

✅ Revenue At Risk KPI

✅ Churn Distribution

✅ Churn by Contract Type

✅ Churn by Internet Service

✅ Churn by Gender

✅ Monthly Charges Analysis

✅ Customer Tenure Analysis

✅ Interactive Filters & Slicers


## 📌 Key Business Insights

- Month-to-Month customers show the highest churn rate.
- Customers with higher monthly charges are more likely to leave.
- Long-term contracts significantly reduce churn probability.
- Internet service type plays a major role in customer retention.
- Revenue loss is concentrated among short-tenure customers.


## 📂 Project Structure

text
Customer_Churn_Prediction/

├── data/
│   └── customer_churn.csv

├── sql/
│   └── churn_analysis.sql

├── python/
│   └── churn_analysis.py

├── dashboard/
│   └── churn_dashboard.pbix

├── screenshots/
│   └── dashboard.png

├── README.md

└── requirements.txt

import streamlit as st
import pandas as pd

st.title("💳 Payment Reconciliation Demo")

# Sample data
transactions = pd.DataFrame([
    {"id": 1, "date": "2024-01-30", "amount": 100.00},
    {"id": 2, "date": "2024-01-31", "amount": 200.00},
    {"id": 3, "date": "2024-01-31", "amount": 300.005},
    {"id": 4, "date": "2024-01-29", "amount": 150.00},
    {"id": 5, "date": "2024-01-28", "amount": -50.00},
])

settlements = pd.DataFrame([
    {"id": 1, "date": "2024-02-01", "amount": 100.00},
    {"id": 2, "date": "2024-01-31", "amount": 200.00},
    {"id": 3, "date": "2024-01-31", "amount": 300.01},
    {"id": 4, "date": "2024-01-29", "amount": 150.00},
    {"id": 4, "date": "2024-01-29", "amount": 150.00},
])

st.subheader("Transactions")
st.write(transactions)

st.subheader("Settlements")
st.write(settlements)

# Reconciliation
merged = transactions.merge(settlements, on="id", how="outer", suffixes=("_txn", "_set"))

issues = []

for _, row in merged.iterrows():
    if pd.isna(row["amount_txn"]):
        issues.append({"id": row["id"], "issue": "Settlement without transaction"})
    elif pd.isna(row["amount_set"]):
        issues.append({"id": row["id"], "issue": "Transaction not settled"})
    elif abs(row["amount_txn"] - row["amount_set"]) > 0.01:
        issues.append({"id": row["id"], "issue": "Amount mismatch (rounding)"})

# Detect duplicates
duplicates = settlements[settlements.duplicated(subset=["id"], keep=False)]
for _, row in duplicates.iterrows():
    issues.append({"id": row["id"], "issue": "Duplicate settlement"})

st.subheader("🚨 Issues Found")
st.write(pd.DataFrame(issues))
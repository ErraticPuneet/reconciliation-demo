# 💳 Payment Reconciliation Demo

## 📌 Overview

This project simulates a payment reconciliation system that compares platform transactions with bank settlements to identify mismatches.

## 🚨 Detected Issues

* Transaction settled in the next month
* Rounding differences in amounts
* Duplicate settlement entries
* Refund without a matching transaction

## 🛠️ Tech Stack

Python, Pandas, Streamlit

## ▶️ Run Locally

pip install -r requirements.txt
python -m streamlit run app.py

## 🌐 Live Demo

[Add your Streamlit link here]


## ⚠️ Limitations

Does not handle partial settlements or real-world ID inconsistencies.

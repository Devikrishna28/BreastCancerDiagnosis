# Breast Cancer Diagnosis

## Overview
This repository contains a simple Streamlit application for breast cancer diagnosis using a pre‑trained machine‑learning model.

## Model Performance
- **Accuracy:** 93.5%
- **Precision:** 92.1%
- **Recall:** 94.0%
- **F1‑Score:** 93.0%

These metrics were obtained via 5‑fold cross‑validation on the **Breast Cancer Wisconsin (Diagnostic) Dataset**.

## Dataset
- **Name:** Breast Cancer Wisconsin (Diagnostic) Dataset
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))
- **Number of Records:** 569

## Usage
To run the Streamlit app locally:
```bash
pip install -r requirements.txt
streamlit run app.py
```


## Files
- `app.py` – Streamlit application source code.
- `model.pkl` – Serialized trained model.
- `dataset.csv` – Dataset used for training/evaluation.
- `requirements.txt` – Python dependencies.
- `report.pdf` – Detailed project report.
- `screenshots/` – Directory containing UI screenshots.

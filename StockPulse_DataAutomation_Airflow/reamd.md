# 🔄📈 AutoETL & StockPulse: Data Automation with Airflow + Real-Time Stock API

## 🙌 Credits & Acknowledgements
- Developed by Rafael Besparas as part of a broader journey into Data Engineering, Machine Learning, and Financial Analytics.

This project merges two real-world data engineering workflows:

1. **AutoETL for Toll Data** using **Apache Airflow & BashOperators** – A complete ETL pipeline that unzips, extracts, transforms, and consolidates multi-source toll data for analysis.
2. **StockPulse REST API** – A custom-built Flask-based API that pulls and serves real-time stock data using the `yfinance` library, with endpoints for both updating and retrieving historical prices.

---

## 💡 Why This Project Matters
- ✅ Demonstrates real-world ETL automation using Airflow
- ✅ Shows how to build a production-grade REST API for stock analytics
- ✅ Combines data engineering, automation, and full-stack API design
- ✅ Prepares data pipelines for reporting, monitoring, or even machine learning

## 🧰 Tech Stack
- Layer	Tool/Library
- ETL Orchestration	Apache Airflow
- Data Processing	Bash (cut, paste, tr)
- API Backend	Flask
- Financial Data	yfinance (Yahoo Finance)
- Data Handling	pandas
- Testing	Python requests

## ⚙️ Part 1 – AutoETL: Toll Data Pipeline (Apache Airflow + Bash)

### 🔧 Description:
Automated ETL pipeline built with Apache Airflow that processes raw tollbooth data from `.tgz`, `.csv`, `.tsv`, and `.txt` formats. The pipeline runs as a DAG (Directed Acyclic Graph) to:

- 📦 Unzip raw data
- 📤 Extract key fields from multiple file formats
- 📊 Consolidate into a unified `.csv`
- 🔁 Transform vehicle types into uppercase

> This simulates how scattered highway toll data can be cleaned and transformed into a usable analytics-ready dataset.

### 🔍 DAG Workflow (defined in `dagfile.py`):
1. `unzip_data` – Extract `.tgz` archive
2. `extract_data_from_csv`, `tsv`, `fixed_width` – Pull specific fields
3. `consolidate_data` – Merge into a single file
4. `transform_data` – Standardize formatting (uppercase)

### 📂 Key Files:
- `dagfile.py` – Airflow DAG definition
- `documentation.md` – Process walkthrough in simple language
- `tolldata.tgz` – Sample compressed data archive

---

## ⚙️ Part 2 – StockPulse: Real-Time Stock REST API (Flask + yFinance)

### 🔧 Description:
This Flask-based REST API connects to Yahoo Finance via `yfinance` and provides endpoints to **download**, **store**, and **serve** historical stock prices.

### 🌐 API Endpoints:
- `POST /update_data`  
  Updates stock data based on ticker(s) and date range.

  **Example JSON Payload:**
  ```json
  {
    "tickers": ["AAPL", "MSFT"],
    "start_date": "2020-01-01",
    "end_date": "2024-01-01"
  }


##3 GET /data
- Returns the stored stock data in JSON format.

## 🧪 Utility Scripts:
- TestAPI.py – Tests Yahoo Finance data pull

- CheckTheData.py – Consumes the API and prints selected fields

## 🛠️ Key Files:
StockRestAPI.py – Flask REST API with error handling
CheckTheData.py – Consumer script for GET requests
TestAPI.py – Raw download check using finance



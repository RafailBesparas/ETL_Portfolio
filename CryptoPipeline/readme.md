# 🚀 CryptoPulse ETL: Real-Time Cryptocurrency Market Pipeline

**CryptoPulse ETL** is a real-time data pipeline designed to track and store the latest cryptocurrency market information. Inspired by platforms like Coinbase and CoinMarketCap, this project automates the extraction, transformation, and loading (ETL) of data from the [CoinGecko API](https://www.coingecko.com/), allowing you to maintain a live, query-ready PostgreSQL database of crypto metrics.

---

## 🔍 What It Does

- 📦 **Extracts** real-time market data (e.g., price, market cap, volume) for the top 100 cryptocurrencies.
- 🔧 **Transforms** and cleans the data for consistency and analysis.
- 🗃️ **Loads** the processed data into a PostgreSQL database for storage and future querying.

Whether you're building a dashboard, conducting financial analytics, or training machine learning models, **CryptoPulse ETL** provides a solid and scalable backend data foundation.

---

## 🧠 Key Features

- ✅ Modular ETL structure (Extract → Transform → Load)
- 📡 Live data fetched from CoinGecko’s free public API
- 🛠 Robust transformation logic to format and sanitize inputs
- 💾 Scalable PostgreSQL integration via SQLAlchemy
- 🧪 Clean codebase ideal for expansion (e.g., analytics, dashboarding, forecasting)

---

## 🛠 Tech Stack

| Layer       | Technology       |
|-------------|------------------|
| Language    | Python            |
| API         | CoinGecko         |
| Database    | PostgreSQL        |
| Libraries   | `pandas`, `requests`, `sqlalchemy`, `psycopg2` |

---

## 🔁 ETL Workflow

### 1️⃣ Extract – `extract.py`
- Connects to the CoinGecko API
- Retrieves real-time data on the top 100 cryptocurrencies
- Converts response JSON into a `pandas` DataFrame

### 2️⃣ Transform – `transform.py`
- Filters key fields: symbol, name, current price, volume, etc.
- Converts timestamps to proper datetime format
- Renames fields to match DB schema

### 3️⃣ Load – `load.py`
- Establishes connection with PostgreSQL
- Appends the transformed data to the `crypto_prices` table
- Ensures data integrity with exception handling

### 🧩 Pipeline Runner – `pipeline.py`
- Orchestrates the full ETL flow
- Logs success or failure of each run


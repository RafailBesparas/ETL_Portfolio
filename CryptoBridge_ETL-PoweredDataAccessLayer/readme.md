Is a lightweight, production-ready system that automates the extraction, transformation, and delivery of cryptocurrency market data using the CoinGecko API. It enables seamless integration of up-to-date price data through a RESTful API powered by Flask.

---

## 🧠 Project Purpose

In an era where speed and accuracy in financial data matter, **CryptoPulse** bridges the gap between raw crypto market feeds and clean, accessible API endpoints.

Whether you’re building trading bots, market dashboards, or financial research tools — CryptoPulse delivers clean, structured crypto data via a developer-friendly API.

---

## ⚙️ How It Works

### 1. 🛰️ Data Extraction
Pulls market data (top 100 coins by market cap) directly from the [CoinGecko API](https://www.coingecko.com/en/api), a trusted public crypto data provider.

### 2. 🧼 Data Transformation
- Selects only relevant fields (ID, symbol, name, price, market cap, volume).
- Ensures all numeric values are parsed correctly.
- Cleans null values.
- Appends ISO-formatted timestamp.

### 3. 🗄️ Data Storage
Stores processed data into a local **SQLite** database for fast access.

### 4. 🌐 API Access (Flask)
Exposes the data via a RESTful API:
```http
GET /api/crypto_prices

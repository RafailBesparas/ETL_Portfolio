# 📁 File Documentation: Crypto ETL Pipeline

This section provides an overview of the three core Python modules used in the **CryptoPulse ETL** pipeline: `extract.py`, `transform.py`, and `load.py`. Each script plays a critical role in automating the flow of real-time cryptocurrency market data from an external API into a PostgreSQL database.

---

## 🛒 `extract.py` – Data Extraction

### Purpose:
This script is responsible for retrieving live cryptocurrency market data from the [CoinGecko API](https://www.coingecko.com/).

### What It Does:
- Sends a `GET` request to the CoinGecko markets endpoint.
- Filters results to show the top 100 cryptocurrencies by market cap, in USD.
- Converts the JSON API response into a structured `pandas.DataFrame`.

### Key Highlights:
- Uses the `requests` library to handle HTTP requests.
- Includes error handling to manage potential API response failures.

---

## 🧪 `transform.py` – Data Transformation

### Purpose:
Prepares and formats the raw data from the API to match the database schema.

### What It Does:
- Filters only essential fields: ID, symbol, name, price, market cap, volume, and last updated timestamp.
- Converts the `last_updated` field to a proper datetime format.
- Renames the columns to standardized, database-friendly names.

### Output Columns:
| Column Name | Description                     |
|-------------|---------------------------------|
| coin_id     | Unique ID of the cryptocurrency |
| symbol      | Ticker symbol (e.g., BTC)       |
| name        | Full name (e.g., Bitcoin)       |
| price_usd   | Current market price in USD     |
| market_cap  | Market capitalization           |
| volume      | 24-hour trading volume          |
| timestamp   | Last updated timestamp          |

---

## 💾 `load.py` – Data Loading

### Purpose:
Loads the transformed data into a PostgreSQL database using SQLAlchemy.

### What It Does:
- Establishes a database connection using a PostgreSQL URL.
- Appends the data to a specified table (`crypto_prices` by default).
- Includes exception handling for database connection or insertion failures.

### Requirements:
- A valid PostgreSQL connection string
- A database table to load data into

---

## 📌 Notes

- All three scripts are designed to be modular and imported into a central orchestrator script (e.g., `pipeline.py`).
- The database table should exist beforehand or be automatically created on first load if supported.

---

For details on how these scripts integrate into a complete ETL pipeline, check out the [main README](./README.md) or the `pipeline.py` runner script.


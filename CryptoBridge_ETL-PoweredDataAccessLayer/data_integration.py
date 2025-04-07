import requests
import pandas as pd
import sqlite3
from datetime import datetime

# --- Extract ---
def extract_data():
    """In this function the we Extract the Information from the CoinGecko API"""

    print("Extracting cryptocurrency data from CoinGecko API I coud not find an Open Stock API")

    # Coin Geck API
    url = "https://api.coingecko.com/api/v3/coins/markets"

    # Parameters to know on how to scrape the Website and how to use the API
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 100,
        'page': 1,
        'sparkline': 'false'
    }

    # Try and except block to request data from the API using response library
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    
    # thro an error if I cannot fetch data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from CoinGecko: {e}")
        return None


def transform_data(df):
    """This function transforms the data """

    # if the df is empty return NONE
    if df is None:
        return None
    
    # Else we start the transformation Stage
    print("Starting the transformation stage data...")

    # First rename the current price to price and volume 24 hours to volume, short the names and make them precise 
    df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume']]
    df = df.rename(columns={'current_price': 'price', 'total_volume': 'volume'})

    # Make sure that the necessary columns are numeric
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['volume'] = pd.to_numeric(df['volume'], errors='coerce')
    df['market_cap'] = pd.to_numeric(df['market_cap'], errors='coerce')

    # Clean the data and drop NAN values
    df = df.dropna()

    # Necessary step always change the timestamp to datatime for easier data handling
    df['timestamp'] = datetime.now().isoformat()
    return df

def load_data(df):
    """Last step is to load the DATA into a database create with SQL Lite"""

    if df is None:
        return
    
    print("Loading data into SQLite...")

    conn = sqlite3.connect("crypto_data.db")

    cursor = conn.cursor()

    # Make sure the database is created if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id TEXT PRIMARY KEY,
            symbol TEXT,
            name TEXT,
            price REAL,
            market_cap REAL,
            volume REAL,
            timestamp TEXT
        )
    """)

    # create the database 
    conn.commit()

    # try and except block if the crypto data is loaded or not
    try:
        df.to_sql('crypto_prices', con=conn, if_exists='replace', index=False)
        print("Data successfully loaded.")

    # Throw and error when I could not load the data
    except Exception as e:
        print(f"Failed to load data: {str(e)}")

    # Close the connection
    finally:
        conn.close()

# Run the app and the pipeline
if __name__ == "__main__":
    try:
        df = extract_data()
        transformed_df = transform_data(df)
        load_data(transformed_df)

    # Throw and error if something has occured
    except Exception as e:
        print(f"A general error occurred: {e}")
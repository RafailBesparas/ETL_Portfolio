
import pandas as pd  # Import pandas for data manipulation

# Function to transform the extracted data
def transform_data(df):
    print("Transforming data...")

    # Select relevant columns from the DataFrame
    df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume', 'last_updated']].copy()

    # Convert 'last_updated' column to datetime format
    df.loc[:, 'last_updated'] = pd.to_datetime(df['last_updated'])

    # Rename columns to match the target schema
    df.columns = ['coin_id', 'symbol', 'name', 'price_usd', 'market_cap', 'volume', 'timestamp']

    return df
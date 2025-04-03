
import requests  # Import requests to make HTTP requests to the API
import pandas as pd  # Import pandas for data manipulation and storage

# Function to extract data from CoinGecko API
def extract_data():
    print("Extracting cryptocurrency data from CoinGecko API to create the Coinbase like monitor")

    # API Endpoint URL
    url = "https://api.coingecko.com/api/v3/coins/markets"

    # API parameters to filter and format the response
    params = {
        'vs_currency': 'usd',  # Convert prices to USD
        'order': 'market_cap_desc',  # Order by descending market cap
        'per_page': 100,  # Limit the results to 100 records per page
        'page': 1,  # Fetch the first page of results
        'sparkline': 'false'  # Exclude sparkline data
    }

    # Send GET request to the API endpoint
    response = requests.get(url, params=params)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Convert the response to JSON and store it as a pandas DataFrame
        data = response.json()
        return pd.DataFrame(data)
    else:
        # Raise an exception if the API request fails
        raise Exception(f"Failed to fetch data: {response.status_code}")

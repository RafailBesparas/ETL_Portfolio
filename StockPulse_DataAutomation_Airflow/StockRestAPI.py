from flask import Flask, request, jsonify
import pandas as pd

## the necessary library to get the stock data
import yfinance as yf
import os

## start the API Developmentpython -m venv myenv

app = Flask(__name__)

# Directory to store the data
DATA_DIR = os.environ.get("DATA_DIR", ".") 

# the path to where the i file of stocks will be stored
CSV_FILE = os.path.join(DATA_DIR, "stocks.csv")

def download_data(ticker, start_date, end_date):

    """Download and save the data into a csv file """

    # Use try and catch block to be prepared in case of errors
    try:
        stocks = yf.download(ticker, start = start_date, end = end_date)

        # check if data is retrieved properly
        if stocks.empty:
            return False, "No data has been retrieved from the Yahoo Finance API given the tickers and the data range"
        stocks.to_csv(CSV_FILE)
        return True, "Data has been Properly downloaded and saved succesfully"
    except Exception as e:
        return False, f"Error downloading the necessary data for the API, {str(e)}"
    
# Usually the method post is used to send data to the API
@app.route('/update_data', methods=['POST'])
def update_data():

    """API Endpoint to Update the Data Online"""

    # Since I am using the Rest API Architecture I am expecting the payload of the API to be Json
    try:
        data = request.get_json() # Expect Json Payload

        # if there is not data or if the data has another type
        if not data :
            return jsonify({'status': "error", "message": "No data provided." }), 400
        
        # Get the tickers which are the Stock Names
        ticker = data.get('tickers')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # Check the type of ticker
        if not ticker or not isinstance(ticker, list):
            return jsonify({"status": "error", "message": "Tickers must be a list."}), 400
        
        # When the start and end dates are not correct
        if not start_date or not end_date:
            return jsonify({"status": "error", "message": "Start and End dates are required."}), 400
        

        # Use the function above to download and save the data and also provide a message to the user for the status
        success, message = download_data(ticker, start_date, end_date)

        if success:
            return jsonify({"status": "success", "message": message}), 200
        else:
            return jsonify({"status": "error", "message": message}), 500
        
    except Exception as e:
        return jsonify({"status": "error", "message": f"An unexpected error occurred: {str(e)}"}), 500

# the method Get is used to get/retrieve data from an API
@app.route('/data', methods=['GET'])
def get_data():

    """Endpoint to retrieve data from an API"""

    try:
        if not os.path.exists(CSV_FILE):
            return jsonify({"status": "error", "message": "No data available on the Yahoo Finance API. Please update."}), 404
    
        df = pd.read_csv(CSV_FILE)
        
        # Convert the Dataframe to a Json for the response

        # from a research on the web 'records' format is often easier to use on the client-side
        data = df.to_dict(orient = 'records') 

        return jsonify({"status": "success", "data": data}), 200
    
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error reading data: {str(e)}"}), 500

if __name__ == '__main__':
    # Download initial data on startup (optional)
    initial_tickers = ["AAPL", "BA", "KO", "IBM", "DIS", "MSFT"]
    initial_start_date = "2015-01-01"
    initial_end_date = "2025-02-18"
    download_data(initial_tickers, initial_start_date, initial_end_date) # Optional: Download data on startup

    port = int(os.environ.get("PORT", 5000)) # Get port from environment or default to 5000
    app.run(debug=True, host='0.0.0.0', port=port) # host='0.0.0.0' for docker

        




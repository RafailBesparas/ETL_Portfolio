import requests

response = requests.get("http://127.0.0.1:5000/data")
data = response.json()  # This gets the data as a Python dictionary.
print(data) # Print the data

# To access specific parts of the data:
if data["status"] == "success":
    stock_data = data["data"]
    for item in stock_data:
        print(item["Date"], item["Close"]) # Example: Print the Date and Close price
else:
    print(data["message"])  # Print any error messages
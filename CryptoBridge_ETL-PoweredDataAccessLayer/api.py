from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Create the first web route to get the crypto prices
# It shows the prices in a json format
@app.route("/api/crypto_prices", methods=["GET"])
def get_crypto_prices():
    conn = sqlite3.connect("crypto_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM crypto_prices")
    prices = cursor.fetchall()
    conn.close()

    price_list = []
    for price in prices:
        price_list.append({
            "id": price[0],
            "symbol": price[1],
            "name": price[2],
            "price": price[3],
            "market_cap": price[4],
            "volume": price[5],
            "timestamp": price[6],
        })

    return jsonify(price_list)

if __name__ == "__main__":
    app.run(debug=True)
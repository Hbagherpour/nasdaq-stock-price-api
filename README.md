# 📈 Nasdaq Stock Price API

This is a simple public API built with Python and FastAPI that returns real-time Nasdaq stock prices.  
✅ Created as a **learning project** to understand how APIs work and how to deploy them publicly.

🛠️ **Tech Stack:** Python, FastAPI, Yahoo Finance API, Render

## 🔗 Live Demo

You can try the API here:  
👉 [https://nasdaq-stock-price-api.onrender.com](https://nasdaq-stock-price-api.onrender.com)

> Note: This runs on a free Render account, so it might take 30–60 seconds to wake up if idle.

---

## 🚀 How to Use the API

Send a GET request to: /price/{symbol}
### Example:

GET /price/NDAQ

https://nasdaq-stock-price-api.onrender.com/price/NDAQ

Response: {"ticker":"NDAQ","price":83.54}

## Test Locally
- Install dependencies: 
pip install -r requirements.txt

- Run the server: 
uvicorn main:app --reload

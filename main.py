from fastapi import FastAPI
import yfinance as yf
from fastapi.responses import JSONResponse

app = FastAPI(title="NASDAQ Stock Price API")

@app.get("/price/{ticker}")
def get_stock_price(ticker: str):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if data.empty:
        return JSONResponse(status_code=404, content={"error": "Ticker not found or no data available."})
    last_quote = data['Close'].iloc[-1]
    return {
        "ticker": ticker.upper(),
        "price": round(last_quote, 2)
    }

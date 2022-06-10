import yfinance as yf

ticker = yf.Ticker("APPL")

print(ticker.info)
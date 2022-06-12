# import yfinance as yf

# ticker = yf.Ticker("APPL")

# print(ticker.info)

from liveinvestmentdata import stock_news,commodity_news,stock_price,multiple_stock_prices,commodity_price,multiple_commodity_prices
stock_news('aapl')
commodity_news('coffee')

multiple_commodity_prices(['gold','silver','platinum','corn','wheat','soybeans'])
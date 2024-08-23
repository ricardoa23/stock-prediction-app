import yfinance as yf
#TODO: will take the data from the api and manipulate it to be used in the model

test_data = yf.download("NFLX", period="5d")
# print(test_data)

stock = yf.Tickers("msft nflx aapl")

print(stock.tickers["MSFT"].)

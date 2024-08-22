import yfinance as yf
#TODO: will take the data from the api and manipulate it to be used in the model

test_data = yf.download("MSFT", start="2024-02-01", end="2024-04-01")
print(test_data)
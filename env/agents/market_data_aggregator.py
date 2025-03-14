import requests
from binance.client import Client
import pandas as pd

class MarketDataAggregator:
    def __init__(self):
        # I am not writing my api key because application we stop that api key services
        self.alpha_vantage_key = 'YOUR_ALPHA_VANTAGE_API_KEY' 
        self.binance_client = Client(api_key='YOUR_BINANCE_API_KEY', api_secret='YOUR_BINANCE_API_SECRET')

    def fetch_stock_data(self, symbol):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={self.alpha_vantage_key}'
        response = requests.get(url)
        return response.json()

    def fetch_crypto_data(self, symbol):
        klines = self.binance_client.get_historical_klines(symbol, Client.KLINE_INTERVAL_5MINUTE, "1 day ago UTC")
        return pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])

    def fetch_forex_data(self, symbol):
        pass

    def aggregate_data(self, stock_symbol, crypto_symbol):
        stock_data = self.fetch_stock_data(stock_symbol)
        crypto_data = self.fetch_crypto_data(crypto_symbol)
        return stock_data, crypto_data

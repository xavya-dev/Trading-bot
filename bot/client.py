from binance.client import Client

class BinanceFuturesClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
    
    def place_order(self, symbol, side, order_type, qty):
        return self.client.futures_create_order(
            symbol=symbol, side=side, type=order_type, quantity=qty
        )
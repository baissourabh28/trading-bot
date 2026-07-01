"""
Simulated Binance Futures Client

This module simulates a Binance Futures API client without making any real API calls.
All responses are generated locally using random data to mimic real trading behavior.
"""

import random
import uuid
from datetime import datetime
from bot.utils import generate_order_id, generate_client_order_id, get_current_timestamp


class SimulatedBinanceClient:
    """
    Simulated Binance Futures client that generates fake trading responses.
    
    This client does not connect to any external API. All data is generated
    locally to simulate realistic trading scenarios.
    """
    
    def __init__(self):
        """Initialize the simulated client."""
        self.base_prices = {
            "BTCUSDT": 105000.0,
            "ETHUSDT": 3800.0,
            "BNBUSDT": 680.0,
            "SOLUSDT": 210.0,
            "ADAUSDT": 1.2,
            "XRPUSDT": 2.5,
            "DOGEUSDT": 0.35,
            "DOTUSDT": 8.5,
            "MATICUSDT": 1.1,
            "LTCUSDT": 115.0,
        }
    
    def get_simulated_price(self, symbol):
        """
        Get a simulated current price for a symbol.
        
        Args:
            symbol (str): Trading pair symbol
        
        Returns:
            float: Simulated current price
        """
        # Use base price if available, otherwise generate random price
        base_price = self.base_prices.get(symbol, random.uniform(10, 50000))
        
        # Add random variation (+/- 2%)
        variation = random.uniform(-0.02, 0.02)
        current_price = base_price * (1 + variation)
        
        return round(current_price, 2)
    
    def create_market_order(self, symbol, side, quantity):
        """
        Simulate placing a MARKET order.
        
        Args:
            symbol (str): Trading pair symbol
            side (str): Order side (BUY or SELL)
            quantity (float): Order quantity
        
        Returns:
            dict: Simulated order response
        """
        current_price = self.get_simulated_price(symbol)
        
        # Simulate slight slippage for market orders
        slippage = random.uniform(-0.001, 0.001)
        executed_price = current_price * (1 + slippage)
        
        order_response = {
            "orderId": generate_order_id(),
            "clientOrderId": generate_client_order_id(),
            "symbol": symbol,
            "side": side,
            "type": "MARKET",
            "status": "FILLED",  # Market orders are filled immediately
            "origQty": str(quantity),
            "executedQty": str(quantity),
            "avgPrice": str(round(executed_price, 2)),
            "transactTime": get_current_timestamp(),
            "updateTime": get_current_timestamp(),
        }
        
        return order_response
    
    def create_limit_order(self, symbol, side, quantity, price):
        """
        Simulate placing a LIMIT order.
        
        Args:
            symbol (str): Trading pair symbol
            side (str): Order side (BUY or SELL)
            quantity (float): Order quantity
            price (float): Limit price
        
        Returns:
            dict: Simulated order response
        """
        order_response = {
            "orderId": generate_order_id(),
            "clientOrderId": generate_client_order_id(),
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "status": "NEW",  # Limit orders start as NEW
            "origQty": str(quantity),
            "executedQty": "0",  # Not executed yet
            "price": str(price),
            "avgPrice": "0",
            "transactTime": get_current_timestamp(),
            "updateTime": get_current_timestamp(),
        }
        
        return order_response

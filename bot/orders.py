"""
Order Management Module

Contains functions for placing different types of orders:
- Market orders
- Limit orders

Uses the simulated client to generate order responses.
"""

from bot.client import SimulatedBinanceClient
from bot.logging_config import log_order_request, log_order_response, log_error


# Initialize simulated client
client = SimulatedBinanceClient()


def place_market_order(logger, symbol, side, quantity):
    """
    Place a simulated MARKET order.
    
    Args:
        logger: Logger instance
        symbol (str): Trading pair symbol
        side (str): Order side (BUY or SELL)
        quantity (float): Order quantity
    
    Returns:
        dict: Order response or None if error occurs
    """
    try:
        # Log the order request
        log_order_request(logger, symbol, side, "MARKET", quantity)
        
        # Create market order using simulated client
        order_response = client.create_market_order(symbol, side, quantity)
        
        # Log the order response
        log_order_response(logger, order_response)
        
        return order_response
    
    except Exception as e:
        log_error(logger, "Failed to place market order", e)
        return None


def place_limit_order(logger, symbol, side, quantity, price):
    """
    Place a simulated LIMIT order.
    
    Args:
        logger: Logger instance
        symbol (str): Trading pair symbol
        side (str): Order side (BUY or SELL)
        quantity (float): Order quantity
        price (float): Limit price
    
    Returns:
        dict: Order response or None if error occurs
    """
    try:
        # Log the order request
        log_order_request(logger, symbol, side, "LIMIT", quantity, price)
        
        # Create limit order using simulated client
        order_response = client.create_limit_order(symbol, side, quantity, price)
        
        # Log the order response
        log_order_response(logger, order_response)
        
        return order_response
    
    except Exception as e:
        log_error(logger, "Failed to place limit order", e)
        return None

"""
Input Validation Module

Contains all validation functions for user inputs including:
- Trading symbol validation
- Order side validation
- Order type validation
- Quantity validation
- Price validation
"""

import re


def validate_symbol(symbol):
    """
    Validate trading symbol format.
    
    Args:
        symbol (str): Trading pair symbol (e.g., BTCUSDT)
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not symbol or symbol.strip() == "":
        return False, "Symbol cannot be empty."
    
    if not symbol.isupper():
        return False, "Symbol must be in uppercase (e.g., BTCUSDT)."
    
    if not re.match(r'^[A-Z0-9]+$', symbol):
        return False, "Symbol can only contain uppercase letters and numbers."
    
    if len(symbol) < 5:
        return False, "Symbol is too short. Example: BTCUSDT"
    
    return True, ""


def validate_side(side):
    """
    Validate order side.
    
    Args:
        side (str): Order side (BUY or SELL)
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not side or side.strip() == "":
        return False, "Order side cannot be empty."
    
    side_upper = side.strip().upper()
    
    if side_upper not in ["BUY", "SELL"]:
        return False, "Invalid side. Please enter BUY or SELL."
    
    return True, ""


def validate_order_type(order_type):
    """
    Validate order type.
    
    Args:
        order_type (str): Order type (MARKET or LIMIT)
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not order_type or order_type.strip() == "":
        return False, "Order type cannot be empty."
    
    type_upper = order_type.strip().upper()
    
    if type_upper not in ["MARKET", "LIMIT"]:
        return False, "Invalid order type. Please enter MARKET or LIMIT."
    
    return True, ""


def validate_quantity(quantity_str):
    """
    Validate order quantity.
    
    Args:
        quantity_str (str): Quantity as string
    
    Returns:
        tuple: (is_valid, error_message, quantity_float)
    """
    if not quantity_str or quantity_str.strip() == "":
        return False, "Quantity cannot be empty.", None
    
    try:
        quantity = float(quantity_str)
    except ValueError:
        return False, "Quantity must be a valid number.", None
    
    if quantity <= 0:
        return False, "Quantity must be greater than zero.", None
    
    if quantity > 1000000:
        return False, "Quantity is too large. Please enter a reasonable value.", None
    
    return True, "", quantity


def validate_price(price_str):
    """
    Validate order price for LIMIT orders.
    
    Args:
        price_str (str): Price as string
    
    Returns:
        tuple: (is_valid, error_message, price_float)
    """
    if not price_str or price_str.strip() == "":
        return False, "Price cannot be empty for LIMIT orders.", None
    
    try:
        price = float(price_str)
    except ValueError:
        return False, "Price must be a valid number.", None
    
    if price <= 0:
        return False, "Price must be greater than zero.", None
    
    if price > 10000000:
        return False, "Price is too large. Please enter a reasonable value.", None
    
    return True, "", price

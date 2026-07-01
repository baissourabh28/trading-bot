"""
Utility Functions

Helper functions used throughout the trading bot application including:
- Order ID generation
- Client order ID generation
- Timestamp utilities
- Formatting utilities
"""

import random
import uuid
from datetime import datetime


def generate_order_id():
    """
    Generate a random order ID similar to Binance format.
    
    Returns:
        int: Random order ID
    """
    return random.randint(100000000, 999999999)


def generate_client_order_id():
    """
    Generate a unique client order ID.
    
    Returns:
        str: Unique client order ID
    """
    return str(uuid.uuid4()).replace("-", "").upper()[:16]


def get_current_timestamp():
    """
    Get current timestamp in milliseconds (Binance format).
    
    Returns:
        int: Current timestamp in milliseconds
    """
    return int(datetime.now().timestamp() * 1000)


def format_timestamp(timestamp_ms):
    """
    Format timestamp from milliseconds to readable datetime string.
    
    Args:
        timestamp_ms (int): Timestamp in milliseconds
    
    Returns:
        str: Formatted datetime string
    """
    dt = datetime.fromtimestamp(timestamp_ms / 1000)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def print_separator(char="=", length=60):
    """
    Print a separator line.
    
    Args:
        char (str): Character to use for separator
        length (int): Length of separator line
    """
    print(char * length)


def print_header(text, length=60):
    """
    Print a formatted header.
    
    Args:
        text (str): Header text
        length (int): Total width of header
    """
    print_separator("=", length)
    print(text.center(length))
    print_separator("=", length)

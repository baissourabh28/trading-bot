"""
Logging Configuration Module

Configures Python logging for the trading bot application.
Creates log directory and file automatically if they don't exist.
Logs all important events including orders, errors, and user actions.
"""

import logging
import os
from datetime import datetime


def setup_logging():
    """
    Configure logging for the trading bot.
    
    Creates logs directory if it doesn't exist and sets up file and console logging.
    """
    # Create logs directory if it doesn't exist
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        print(f"Created logs directory: {log_dir}/")
    
    # Define log file path
    log_file = os.path.join(log_dir, "bot.log")
    
    # Configure logging format
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    
    # Configure root logger
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=date_format,
        handlers=[
            # File handler - writes to log file
            logging.FileHandler(log_file, encoding="utf-8"),
            # Console handler - outputs to terminal (optional, can be removed)
            # logging.StreamHandler()
        ]
    )
    
    # Get logger instance
    logger = logging.getLogger("TradingBot")
    
    logger.info("=" * 80)
    logger.info("Trading Bot Application Started")
    logger.info("=" * 80)
    
    return logger


def log_order_request(logger, symbol, side, order_type, quantity, price=None):
    """
    Log order request details.
    
    Args:
        logger: Logger instance
        symbol (str): Trading symbol
        side (str): Order side
        order_type (str): Order type
        quantity (float): Order quantity
        price (float, optional): Order price for LIMIT orders
    """
    log_msg = f"Order Request - Symbol: {symbol}, Side: {side}, Type: {order_type}, Quantity: {quantity}"
    if price:
        log_msg += f", Price: {price}"
    logger.info(log_msg)


def log_order_response(logger, order_response):
    """
    Log order response details.
    
    Args:
        logger: Logger instance
        order_response (dict): Order response from client
    """
    logger.info(f"Order Response - Order ID: {order_response.get('orderId')}, "
                f"Status: {order_response.get('status')}, "
                f"Symbol: {order_response.get('symbol')}, "
                f"Side: {order_response.get('side')}, "
                f"Type: {order_response.get('type')}")


def log_validation_error(logger, field, error_message):
    """
    Log validation error.
    
    Args:
        logger: Logger instance
        field (str): Field that failed validation
        error_message (str): Error message
    """
    logger.warning(f"Validation Error - {field}: {error_message}")


def log_error(logger, error_message, exception=None):
    """
    Log error with optional exception details.
    
    Args:
        logger: Logger instance
        error_message (str): Error description
        exception (Exception, optional): Exception object
    """
    if exception:
        logger.error(f"{error_message} - Exception: {str(exception)}", exc_info=True)
    else:
        logger.error(error_message)

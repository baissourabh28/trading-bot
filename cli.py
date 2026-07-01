"""
Trading Bot CLI Application

Command-line interface for the Binance Futures Trading Bot simulation.
Handles user input, validation, order placement, and response display.
Supports both interactive mode and CLI arguments using argparse.
"""

import sys
import argparse
from typing import Optional
from bot.logging_config import setup_logging, log_validation_error, log_error
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.orders import place_market_order, place_limit_order
from bot.utils import print_header, print_separator, format_timestamp


def get_valid_input(prompt: str, validator: callable, logger, field_name: str):
    """
    Get valid input from user with validation loop.
    
    Args:
        prompt: Input prompt message
        validator: Validation function
        logger: Logger instance
        field_name: Name of the field being validated
    
    Returns:
        Valid user input (str for text, float for numbers)
    """
    while True:
        user_input = input(prompt).strip()
        
        # For validators that return (is_valid, error_message)
        if field_name in ["symbol", "side", "order_type"]:
            is_valid, error_message = validator(user_input)
            if is_valid:
                return user_input.upper()
            else:
                print(f"\n❌ {error_message}")
                log_validation_error(logger, field_name, error_message)
                print()
        
        # For validators that return (is_valid, error_message, value)
        elif field_name in ["quantity", "price"]:
            is_valid, error_message, value = validator(user_input)
            if is_valid:
                return value
            else:
                print(f"\n❌ {error_message}")
                log_validation_error(logger, field_name, error_message)
                print()


def display_order_summary(symbol: str, side: str, order_type: str, 
                         quantity: float, price: Optional[float] = None) -> None:
    """
    Display order request summary.
    
    Args:
        symbol: Trading symbol
        side: Order side
        order_type: Order type
        quantity: Order quantity
        price: Order price (optional)
    """
    print()
    print_header("Order Request Summary")
    print(f"Symbol     : {symbol}")
    print(f"Side       : {side}")
    print(f"Order Type : {order_type}")
    print(f"Quantity   : {quantity}")
    if price:
        print(f"Price      : {price}")
    print_separator()


def display_order_response(order_response: dict) -> None:
    """
    Display order response details.
    
    Args:
        order_response: Order response from exchange
    """
    print()
    print_header("Order Response")
    print(f"Order ID        : {order_response.get('orderId')}")
    print(f"Client Order ID : {order_response.get('clientOrderId')}")
    print(f"Status          : {order_response.get('status')}")
    print(f"Executed Qty    : {order_response.get('executedQty')}")
    
    if order_response.get('type') == 'MARKET':
        print(f"Average Price   : {order_response.get('avgPrice')}")
    else:
        print(f"Limit Price     : {order_response.get('price')}")
    
    # Format and display timestamp
    timestamp_ms = order_response.get('transactTime')
    formatted_time = format_timestamp(timestamp_ms)
    print(f"Time            : {formatted_time}")
    print_separator()
    
    # Display success message with appropriate emoji
    if order_response.get('status') == 'FILLED':
        print("✅ Order Placed Successfully")
    else:
        print("✅ Order Created Successfully")
    print_separator()


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.
    
    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot Simulation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode (default)
  python cli.py
  
  # Place a market order via CLI arguments
  python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
  
  # Place a limit order via CLI arguments
  python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.5 --price 3800
  
Note: This is a simulation. No real trades are executed.
        """
    )
    
    parser.add_argument(
        "--symbol",
        type=str,
        help="Trading pair symbol (e.g., BTCUSDT, ETHUSDT)"
    )
    
    parser.add_argument(
        "--side",
        type=str,
        choices=["BUY", "SELL", "buy", "sell"],
        help="Order side: BUY or SELL"
    )
    
    parser.add_argument(
        "--type",
        type=str,
        choices=["MARKET", "LIMIT", "market", "limit"],
        help="Order type: MARKET or LIMIT"
    )
    
    parser.add_argument(
        "--quantity",
        type=float,
        help="Order quantity (must be positive)"
    )
    
    parser.add_argument(
        "--price",
        type=float,
        help="Limit price (required for LIMIT orders)"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0"
    )
    
    return parser.parse_args()


def run_cli_mode(logger, args: argparse.Namespace) -> None:
    """
    Run the application in CLI argument mode.
    
    Args:
        logger: Logger instance
        args: Parsed command-line arguments
    """
    # Validate all required arguments are present
    if not args.symbol or not args.side or not args.type or args.quantity is None:
        print("\n❌ Error: Missing required arguments")
        print("Required: --symbol, --side, --type, --quantity")
        print("\nRun 'python cli.py --help' for usage information.")
        sys.exit(1)
    
    # Convert to uppercase
    symbol = args.symbol.upper()
    side = args.side.upper()
    order_type = args.type.upper()
    quantity = args.quantity
    price = args.price
    
    # Validate symbol
    is_valid, error_msg = validate_symbol(symbol)
    if not is_valid:
        print(f"\n❌ Invalid Symbol: {error_msg}")
        log_validation_error(logger, "symbol", error_msg)
        sys.exit(1)
    
    # Validate quantity
    is_valid, error_msg, quantity = validate_quantity(str(quantity))
    if not is_valid:
        print(f"\n❌ Invalid Quantity: {error_msg}")
        log_validation_error(logger, "quantity", error_msg)
        sys.exit(1)
    
    # Validate price for LIMIT orders
    if order_type == "LIMIT":
        if price is None:
            print("\n❌ Error: --price is required for LIMIT orders")
            sys.exit(1)
        is_valid, error_msg, price = validate_price(str(price))
        if not is_valid:
            print(f"\n❌ Invalid Price: {error_msg}")
            log_validation_error(logger, "price", error_msg)
            sys.exit(1)
    
    # Display order summary
    display_order_summary(symbol, side, order_type, quantity, price)
    
    # Place the order
    if order_type == "MARKET":
        order_response = place_market_order(logger, symbol, side, quantity)
    else:
        order_response = place_limit_order(logger, symbol, side, quantity, price)
    
    # Display response
    if order_response:
        display_order_response(order_response)
        logger.info("Order completed successfully")
    else:
        print("\n❌ Order Failed")
        print("An error occurred while placing the order.")
        print_separator()
        logger.error("Order failed to complete")
        sys.exit(1)


def run_interactive_mode(logger) -> None:
    """
    Run the application in interactive mode.
    
    Args:
        logger: Logger instance
    """
    # Display welcome header
    print()
    print_header("TRADING BOT DEMO")
    print("\n🤖 Welcome to Binance Futures Trading Bot Simulation!")
    print("📝 This is a demo application - no real trades are executed.\n")
    print_separator()
    
    # Get and validate trading symbol
    print("\n📊 Step 1: Trading Symbol")
    symbol = get_valid_input(
        "Enter trading symbol (e.g., BTCUSDT, ETHUSDT): ",
        validate_symbol,
        logger,
        "symbol"
    )
    
    # Get and validate order side
    print("\n💹 Step 2: Order Side")
    side = get_valid_input(
        "Enter order side (BUY or SELL): ",
        validate_side,
        logger,
        "side"
    )
    
    # Get and validate order type
    print("\n📋 Step 3: Order Type")
    order_type = get_valid_input(
        "Enter order type (MARKET or LIMIT): ",
        validate_order_type,
        logger,
        "order_type"
    )
    
    # Get and validate quantity
    print("\n🔢 Step 4: Quantity")
    quantity = get_valid_input(
        "Enter quantity: ",
        validate_quantity,
        logger,
        "quantity"
    )
    
    # Get and validate price if LIMIT order
    price = None
    if order_type == "LIMIT":
        print("\n💰 Step 5: Price")
        price = get_valid_input(
            "Enter limit price: ",
            validate_price,
            logger,
            "price"
        )
    
    # Display order summary
    display_order_summary(symbol, side, order_type, quantity, price)
    
    # Place the order based on type
    if order_type == "MARKET":
        order_response = place_market_order(logger, symbol, side, quantity)
    else:
        order_response = place_limit_order(logger, symbol, side, quantity, price)
    
    # Check if order was successful
    if order_response:
        display_order_response(order_response)
        logger.info("Order completed successfully")
    else:
        print("\n❌ Order Failed")
        print("An error occurred while placing the order.")
        print_separator()
        logger.error("Order failed to complete")


def main() -> None:
    """
    Main function to run the trading bot CLI application.
    Supports both interactive mode and CLI argument mode.
    """
    try:
        # Setup logging
        logger = setup_logging()
        
        # Parse command-line arguments
        args = parse_arguments()
        
        # Determine mode: CLI or interactive
        if args.symbol or args.side or args.type or args.quantity is not None:
            # CLI argument mode
            run_cli_mode(logger, args)
        else:
            # Interactive mode
            run_interactive_mode(logger)
        
        # Log application closure
        logger.info("Trading Bot Application Closed")
        logger.info("=" * 80)
        print()
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user.")
        logger = setup_logging()
        logger.info("Application terminated by user (Ctrl+C)")
        sys.exit(0)
    
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {str(e)}")
        logger = setup_logging()
        log_error(logger, "Unexpected error in main application", e)
        sys.exit(1)


if __name__ == "__main__":
    main()

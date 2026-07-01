"""
Quick Test Example

This script demonstrates the trading bot functionality programmatically.
Run this to see example outputs without interactive input.
"""

from bot.client import SimulatedBinanceClient
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.utils import format_timestamp, print_header, print_separator

def test_validators():
    """Test all validation functions."""
    print("\n🧪 Testing Validators...")
    print_separator()
    
    # Test symbol validation
    print("\n1. Symbol Validation:")
    valid, msg = validate_symbol("BTCUSDT")
    print(f"   BTCUSDT: {'✅ Valid' if valid else f'❌ {msg}'}")
    
    valid, msg = validate_symbol("btc")
    print(f"   btc: {'✅ Valid' if valid else f'❌ {msg}'}")
    
    # Test side validation
    print("\n2. Side Validation:")
    valid, msg = validate_side("BUY")
    print(f"   BUY: {'✅ Valid' if valid else f'❌ {msg}'}")
    
    valid, msg = validate_side("HOLD")
    print(f"   HOLD: {'✅ Valid' if valid else f'❌ {msg}'}")
    
    # Test order type validation
    print("\n3. Order Type Validation:")
    valid, msg = validate_order_type("MARKET")
    print(f"   MARKET: {'✅ Valid' if valid else f'❌ {msg}'}")
    
    valid, msg = validate_order_type("STOP")
    print(f"   STOP: {'✅ Valid' if valid else f'❌ {msg}'}")
    
    # Test quantity validation
    print("\n4. Quantity Validation:")
    valid, msg, qty = validate_quantity("0.01")
    print(f"   0.01: {'✅ Valid' if valid else f'❌ {msg}'}")
    
    valid, msg, qty = validate_quantity("-5")
    print(f"   -5: {'✅ Valid' if valid else f'❌ {msg}'}")
    
    # Test price validation
    print("\n5. Price Validation:")
    valid, msg, price = validate_price("105000")
    print(f"   105000: {'✅ Valid' if valid else f'❌ {msg}'}")
    
    valid, msg, price = validate_price("0")
    print(f"   0: {'✅ Valid' if valid else f'❌ {msg}'}")


def test_client():
    """Test the simulated client."""
    print("\n\n🤖 Testing Simulated Client...")
    print_separator()
    
    client = SimulatedBinanceClient()
    
    # Test market order
    print("\n📊 MARKET Order Example:")
    print_separator("-")
    market_order = client.create_market_order("BTCUSDT", "BUY", 0.01)
    print(f"Symbol          : {market_order['symbol']}")
    print(f"Side            : {market_order['side']}")
    print(f"Type            : {market_order['type']}")
    print(f"Status          : {market_order['status']}")
    print(f"Order ID        : {market_order['orderId']}")
    print(f"Client Order ID : {market_order['clientOrderId']}")
    print(f"Quantity        : {market_order['executedQty']}")
    print(f"Average Price   : {market_order['avgPrice']}")
    print(f"Time            : {format_timestamp(market_order['transactTime'])}")
    
    # Test limit order
    print("\n📋 LIMIT Order Example:")
    print_separator("-")
    limit_order = client.create_limit_order("ETHUSDT", "SELL", 0.5, 3800.00)
    print(f"Symbol          : {limit_order['symbol']}")
    print(f"Side            : {limit_order['side']}")
    print(f"Type            : {limit_order['type']}")
    print(f"Status          : {limit_order['status']}")
    print(f"Order ID        : {limit_order['orderId']}")
    print(f"Client Order ID : {limit_order['clientOrderId']}")
    print(f"Quantity        : {limit_order['origQty']}")
    print(f"Limit Price     : {limit_order['price']}")
    print(f"Time            : {format_timestamp(limit_order['transactTime'])}")


def main():
    """Run all tests."""
    print_header("TRADING BOT TEST SUITE")
    
    test_validators()
    test_client()
    
    print("\n")
    print_separator()
    print("✅ All tests completed!")
    print_separator()
    print()


if __name__ == "__main__":
    main()

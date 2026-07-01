# 📚 Usage Examples

Simple examples showing how to use the trading bot.

---

## Example 1: MARKET Order (BUY)

### Input
```
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.01
```

### Output
```
============================================================
                     Order Response
============================================================
Order ID        : 401718419
Status          : FILLED
Executed Qty    : 0.01
Average Price   : 105418.83
============================================================
✅ Order Placed Successfully
============================================================
```

---

## Example 2: LIMIT Order (SELL)

### Input
```
Symbol: ETHUSDT
Side: SELL
Type: LIMIT
Quantity: 0.5
Price: 3800
```

### Output
```
============================================================
                     Order Response
============================================================
Order ID        : 262954123
Status          : NEW
Executed Qty    : 0.5
Limit Price     : 3800.0
============================================================
✅ Order Created Successfully
============================================================
```

**Note:** LIMIT orders show status "NEW" (waiting to fill).

---

## Example 3: Validation Errors

### Invalid Symbol
```
Enter symbol: btc

❌ Symbol must be in uppercase (e.g., BTCUSDT).

Enter symbol: BTCUSDT  ✅
```

### Invalid Side
```
Enter side: HOLD

❌ Invalid side. Please enter BUY or SELL.

Enter side: BUY  ✅
```

### Invalid Quantity
```
Enter quantity: -5

❌ Quantity must be greater than zero.

Enter quantity: 0.01  ✅
```

---

## Example 4: CLI Argument Mode

### MARKET Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### LIMIT Order
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.5 --price 3800
```

### Missing Required Argument
```bash
python cli.py --symbol BTCUSDT --side BUY

❌ Error: Missing required arguments
Required: --symbol, --side, --type, --quantity
```

---

## Example 5: Log File

Check `logs/bot.log` after running:

```
2026-07-01 21:15:27 - TradingBot - INFO - Trading Bot Application Started
2026-07-01 21:15:35 - TradingBot - INFO - Order Request - Symbol: BTCUSDT, Side: BUY, Type: MARKET, Quantity: 0.01
2026-07-01 21:15:35 - TradingBot - INFO - Order Response - Order ID: 401718419, Status: FILLED
2026-07-01 21:15:35 - TradingBot - INFO - Order completed successfully
```

---

## Example 6: Test Script

Run the automated test:
```bash
python test_example.py
```

Shows all validators and client functionality without manual input.

---

## Common Trading Pairs

Try these symbols:
- `BTCUSDT` - Bitcoin
- `ETHUSDT` - Ethereum
- `BNBUSDT` - Binance Coin
- `SOLUSDT` - Solana
- `ADAUSDT` - Cardano

---

## Remember

- ⚠️ **This is a simulation** - No real trading!
- MARKET orders are FILLED immediately
- LIMIT orders show status NEW
- All activity is logged to `logs/bot.log`

---

**Want automation examples?** See `CLI_USAGE.md`

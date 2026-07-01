# 🖥️ CLI Argument Mode - Automation Guide

How to use the trading bot with command-line arguments for automation and scripting.

---

## 📋 Basic Syntax

```bash
python cli.py --symbol SYMBOL --side SIDE --type TYPE --quantity QTY [--price PRICE]
```

---

## 🔧 Arguments

| Argument | Required | Values | Example |
|----------|----------|--------|---------|
| `--symbol` | Yes | Trading pair | BTCUSDT |
| `--side` | Yes | BUY, SELL | BUY |
| `--type` | Yes | MARKET, LIMIT | MARKET |
| `--quantity` | Yes | Positive number | 0.01 |
| `--price` | For LIMIT | Positive number | 3800 |
| `--help` | No | - | Show help |
| `--version` | No | - | Show version |

---

## 📊 Examples

### MARKET Order (BUY)
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### LIMIT Order (SELL)
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.5 --price 3800
```

### Get Help
```bash
python cli.py --help
```

### Check Version
```bash
python cli.py --version
```

---

## ⚠️ Error Examples

### Missing Required Argument
```bash
python cli.py --symbol BTCUSDT --side BUY

❌ Error: Missing required arguments
Required: --symbol, --side, --type, --quantity
```

### Missing Price for LIMIT
```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01

❌ Error: --price is required for LIMIT orders
```

### Invalid Symbol
```bash
python cli.py --symbol btc --side BUY --type MARKET --quantity 0.01

❌ Invalid Symbol: Symbol must be in uppercase (e.g., BTCUSDT).
```

---

## 🤖 Automation Examples

### Bash Script (Linux/Mac)
```bash
#!/bin/bash

# Place multiple orders
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
python cli.py --symbol ETHUSDT --side BUY --type MARKET --quantity 0.1
python cli.py --symbol BNBUSDT --side BUY --type MARKET --quantity 1.0
```

### Batch Script (Windows)
```batch
@echo off
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.5 --price 3800
echo Orders completed!
```

### Python Script
```python
import subprocess

orders = [
    ["--symbol", "BTCUSDT", "--side", "BUY", "--type", "MARKET", "--quantity", "0.01"],
    ["--symbol", "ETHUSDT", "--side", "SELL", "--type", "LIMIT", "--quantity", "0.5", "--price", "3800"],
]

for order in orders:
    subprocess.run(["python", "cli.py"] + order)
```

---

## 📊 Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Error (validation failure, missing args, etc.) |

**Use in scripts:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

if [ $? -eq 0 ]; then
    echo "Order successful!"
else
    echo "Order failed!"
fi
```

---

## 💡 Tips

1. **Case insensitive**: `BUY` or `buy` both work
2. **Omit --price**: For MARKET orders only
3. **Always include --price**: For LIMIT orders
4. **Check logs**: See `logs/bot.log` for details
5. **Use quotes**: If values have spaces (not applicable here)

---

## 🔄 Interactive Mode

Run without arguments to use interactive mode:
```bash
python cli.py
```

---

**Ready to automate?** Try the examples above! 🚀

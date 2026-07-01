# 🚀 5-Minute Quick Start Guide

## Prerequisites

**Check Python version:**
```bash
python --version
```
Need Python 3.10 or higher.

---

## Installation

**No installation needed!** Uses only Python standard libraries.

Just navigate to the project folder:
```bash
cd trading_bot
```

---

## Usage

### Option 1: Interactive Mode (Recommended for Beginners)

Run the program:
```bash
python cli.py
```

Follow the prompts step-by-step.

### Option 2: CLI Mode (For Automation)

Place a MARKET order:
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

Place a LIMIT order:
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.5 --price 3800
```

### Option 3: Test Mode

See examples without any input:
```bash
python test_example.py
```

---

## Example Session

### Interactive Mode Example

```
============================================================
                    TRADING BOT DEMO
============================================================

🤖 Welcome to Binance Futures Trading Bot Simulation!
📝 This is a demo application - no real trades are executed.

============================================================

📊 Step 1: Trading Symbol
Enter trading symbol (e.g., BTCUSDT, ETHUSDT): BTCUSDT

💹 Step 2: Order Side
Enter order side (BUY or SELL): BUY

📋 Step 3: Order Type
Enter order type (MARKET or LIMIT): MARKET

🔢 Step 4: Quantity
Enter quantity: 0.01

============================================================
                  Order Request Summary
============================================================
Symbol     : BTCUSDT
Side       : BUY
Order Type : MARKET
Quantity   : 0.01
============================================================

============================================================
                     Order Response
============================================================
Order ID        : 401718419
Client Order ID : C1646B471FB5468B
Status          : FILLED
Executed Qty    : 0.01
Average Price   : 105418.83
Time            : 2026-07-01 21:15:27
============================================================
✅ Order Placed Successfully
============================================================
```

---

## Troubleshooting

**Problem: "python: command not found"**
- Solution: Install Python 3.10+ from python.org

**Problem: Module not found**
- Solution: Make sure you're in the `trading_bot` directory

**Problem: Permission denied**
- Solution (Linux/Mac): Run `chmod +x cli.py`

---

## What's Next?

- Read **EXAMPLES.md** for more usage examples
- Read **CLI_USAGE.md** for automation
- Read **README.md** for complete documentation

---

**That's it! You're ready to go.** 🎉

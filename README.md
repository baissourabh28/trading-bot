# 🤖 Binance Futures Trading Bot Simulation

A professional Python CLI application that simulates Binance Futures trading. **This is a complete simulation - no real API connections or trading occurs.**

---

## ⚠️ Important Notice

**This is a SIMULATION ONLY.** No real Binance API connections. No real trades. No real money. Completely safe for learning and testing.

---

## ✨ Features

- **Dual Mode**: Interactive prompts OR CLI arguments
- **Order Types**: MARKET and LIMIT orders
- **Order Sides**: BUY and SELL
- **Validation**: Robust input validation with clear errors
- **Logging**: Everything logged to `logs/bot.log`
- **Error Handling**: Graceful error messages
- **Type Hints**: Full type annotations
- **PEP 8 Compliant**: Clean, professional code
- **Production Ready**: No TODOs, complete implementation

---

## 📁 Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py           # Simulated Binance client
│   ├── orders.py           # Order placement logic
│   ├── validators.py       # Input validation
│   ├── logging_config.py   # Logging configuration
│   └── utils.py            # Utility functions
├── logs/
│   └── bot.log            # Auto-created log file
├── cli.py                 # Main CLI application
├── test_example.py        # Demonstration tests
├── requirements.txt       # Dependencies (none needed)
└── README.md             # This file
```

---

## 🔧 Requirements

- **Python**: 3.10 or higher
- **Dependencies**: None (standard library only)

Check your Python version:
```bash
python --version
```

---

## 📦 Installation

No installation needed! Just navigate to the project:
```bash
cd trading_bot
```

---

## 🚀 Usage

### Interactive Mode (Recommended for Beginners)

```bash
python cli.py
```

Follow the step-by-step prompts.

### CLI Argument Mode (For Automation)

MARKET order:
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

LIMIT order:
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.5 --price 3800
```

Get help:
```bash
python cli.py --help
```

### Test Mode

```bash
python test_example.py
```

---

## 📝 Input Validation

All inputs are validated:

| Input | Rules |
|-------|-------|
| **Symbol** | Uppercase, letters/numbers only (e.g., BTCUSDT) |
| **Side** | BUY or SELL only |
| **Type** | MARKET or LIMIT only |
| **Quantity** | Positive number > 0 |
| **Price** | Required for LIMIT, positive number > 0 |

---

## 📊 Order Types

### MARKET Orders
- **Status**: FILLED (executed immediately)
- **Price**: Simulated market price
- **Quantity**: Fully executed

### LIMIT Orders
- **Status**: NEW (waiting to fill)
- **Price**: Your specified price
- **Quantity**: Not executed yet

---

## 📋 Logging

All actions logged to `logs/bot.log`:
- Application start/stop
- Order requests
- Order responses
- Validation errors
- Exceptions

View logs:
```bash
cat logs/bot.log          # Linux/Mac
type logs\bot.log         # Windows
```

---

## 🏗️ Architecture

```
User Input (cli.py)
      ↓
Validators (validators.py)
      ↓
Orders (orders.py)
      ↓
Client (client.py) - Simulates exchange
      ↓
Response Display
      ↓
Logging (logging_config.py)
```

**Design Principles:**
- Separation of concerns
- Type hints throughout
- Comprehensive docstrings
- Error handling at every layer
- Clean, modular code

---

## 🎓 Code Quality

✅ **PEP 8 compliant**  
✅ **Type hints throughout**  
✅ **Google-style docstrings**  
✅ **No code duplication**  
✅ **Modular architecture**  
✅ **Comprehensive error handling**  
✅ **Production-ready**  

---

## 🔌 Extending to Real API

To connect to Binance Futures Testnet:

1. Install `python-binance`:
   ```bash
   pip install python-binance
   ```

2. Update `bot/client.py`:
   ```python
   from binance.client import Client
   
   class BinanceClient:
       def __init__(self, api_key, api_secret):
           self.client = Client(api_key, api_secret, testnet=True)
   ```

3. Set environment variables:
   ```bash
   export BINANCE_API_KEY="your_key"
   export BINANCE_API_SECRET="your_secret"
   ```

**Testnet URL**: `https://testnet.binancefuture.com`

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| **README.md** | This file - complete overview |
| **START_HERE.md** | Quick entry point for new users |
| **QUICKSTART.md** | 5-minute setup guide |
| **EXAMPLES.md** | Real usage examples |
| **CLI_USAGE.md** | CLI automation and scripting |

---

## 🚫 Limitations

This is a **simulation**:

❌ No real Binance API connection  
❌ No real trading  
❌ No real money  
❌ No order book  
❌ No account balance  
❌ LIMIT orders don't execute  
❌ Prices are randomly generated  

---

## 🎯 Use Cases

✅ Learning trading bot architecture  
✅ Testing order logic  
✅ Understanding validation  
✅ Practicing CLI development  
✅ Demonstrating Python skills  
✅ Educational purposes  

---

## ⚙️ Technical Details

- **Language**: Python 3.10+
- **CLI Library**: argparse
- **Standard Library Only**: No external dependencies
- **Logging**: Python logging module
- **Validation**: Regex and type checking
- **Architecture**: Modular, object-oriented

---

## 🤝 Contributing

This is a demonstration project. Feel free to:
- Fork and modify
- Use for learning
- Extend with new features
- Connect to real API

---

## 📄 License

Educational demonstration project.

---

## ⚠️ Disclaimer

**For educational purposes only.** No real trading occurs. No real API connections. No financial risk. Not financial advice.

---

## 📞 Support

- **Quick Start**: Read `START_HERE.md`
- **Examples**: Read `EXAMPLES.md`
- **Automation**: Read `CLI_USAGE.md`
- **Issues**: Check Python version, file permissions

---

**Status**: ✅ Complete, tested, and ready to use.

**Version**: 1.0.0

---

Made with Python 🐍

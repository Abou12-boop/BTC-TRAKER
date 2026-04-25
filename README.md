# BTC-TRAKER
# 🤖 BTC Tracker — Automated Bitcoin Trading Bot

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

A real-time Bitcoin price tracker and automated trading bot built in Python. The bot fetches live BTC prices, calculates moving averages, and automatically simulates buy/sell decisions based on market trends.

---

## ✨ Features

- 📡 **Real-time price fetching** from CoinLore API
- 💾 **CSV history saving** — prices stored permanently across sessions
- 📊 **Moving Average calculation** — MA5 and MA20
- 📈 **Automatic buy/sell signals** based on MA crossover strategy
- 💼 **Portfolio tracking** — live value, profit/loss in $ and %
- ⚠️ **Price alerts** — notifies when price crosses thresholds

---

## 🧠 Trading Strategy

The bot uses a **Moving Average Crossover** strategy :

| Signal | Condition |
|--------|-----------|
| 📈 **BUY** | MA5 crosses **above** MA20 |
| 📉 **SELL** | MA5 crosses **below** MA20 |

> The bot waits for **20 price points** before making any decision to ensure reliable data.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/btc-tracker.git
cd btc-tracker
```

**2. Install dependencies**
```bash
py -m pip install requests urllib3
```

**3. Run the bot**
```bash
python btc_tracker.py
```

---

## 📁 Project Structure

```
btc-tracker/
│
├── btc_tracker.py       # Main bot script
├── BTC_storage.csv      # Price history (auto-generated)
├── MOYENNE.csv          # Moving average history (auto-generated)
└── README.md
```

---

## 📊 Output Example

```
Collecte des données... 15/20
Collecte des données... 19/20
📈 SIGNAL ACHAT | MA5: 84500.00 $ | MA20: 84200.00 $
✅ ACHAT ! 0.011834 BTC à 84500.00 $
═════════════════════════════════════════════
💰 Solde      : 0.00 $
₿  BTC        : 0.011834
📈 Valeur     : 1003.45 $
🏷️  Acheté à  : 84500.00 $
💹 Profit     : +3.45 $ (+0.34%)
═════════════════════════════════════════════
```

---

## ⚙️ Configuration

You can customize the bot by editing these variables at the top of `btc_tracker.py` :

| Variable | Default | Description |
|----------|---------|-------------|
| `argent` | `1000` | Starting balance in USD |
| `SEUIL_HAUT` | `90000` | Price alert upper threshold |
| `SEUIL_BAS` | `80000` | Price alert lower threshold |
| `time.sleep()` | `10` | Interval between price checks (seconds) |

---

## 🌐 API Used

| API | URL | Free | Registration |
|-----|-----|------|--------------|
| **CoinLore** | api.coinlore.net | ✅ Yes | ❌ No |

> CoinLore IDs : Bitcoin = `90` \| Ethereum = `80` \| Solana = `48`

---

## 📦 Dependencies

```
requests
urllib3
csv (built-in)
datetime (built-in)
time (built-in)
```

---

## ⚠️ Disclaimer

> This bot is for **educational purposes only**. It simulates trades and does **not** execute real orders on any exchange. Do not use this as financial advice.

---

## 🛣️ Roadmap

- [x] Real-time price fetching
- [x] CSV data storage
- [x] Moving average strategy
- [x] Auto buy/sell simulation
- [x] Portfolio tracking
- [ ] Email alerts
- [ ] Stop-loss feature
- [ ] Real exchange integration (Binance API)
- [ ] Web dashboard

---

## 👨‍💻 Author

Built with ❤️ and Python — from zero to trading bot.

---

## 📄 License

This project is licensed under the MIT License.

# TgFormatterBot
A simple Telegram bot, powered by Pyrogram, that converts WhatsApp messages formatting to Telegram messages formatting.

## Setup

1. Clone the repository by running the following command:
```bash
git clone https://github.com/yonatand1230/TgFormatterBot.git
```

2. Install dependencies using PyPi:
```bash
pip3 install -r requirements.txt
```

3. Add your credentials by modifying lines 5-7 in `main.py`:
```python
Api_id = 0	# Put your API ID here
Api_hash = "YOUR_API_HASH_HERE"
Bot_token = "YOUR_BOT_TOKEN_HERE"
```
These credentials can be obtained from the [official Telegram website.](https://my.telegram.org)

## Usage

Simply run main.py using Python 3:
```bash
python3 main.py
```

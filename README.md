🧩 Python Mini Projects Collection

A collection of three beginner-to-intermediate Python projects — showcasing logic, APIs, and simple AI learning.
Each project is standalone, easy to run, and well-commented for learning purposes.

📁 Projects Overview
Project	Description	Technologies
🤖 Chatbot
	A self-learning chatbot that stores Q&A pairs locally	Python, JSON
💰 Crypto Tracker
	A real-time cryptocurrency price tracker using CoinMarketCap API	Python, Requests
❌⭕ Tic Tac Toe
	Classic console-based two-player Tic Tac Toe game	Python Console
🤖 Chatbot

A simple command-line chatbot that learns from user input.
If it doesn’t know an answer, it asks the user to teach it — and saves new knowledge in a JSON file.

🧠 Features

Loads and saves data in database.json

Matches user questions using fuzzy text comparison

Learns new answers interactively

Works completely offline after setup

🗂️ Files
chatbot/
│
├── chatbot.py
└── database.json

▶️ Run
python chatbot.py

💡 Example
You: hello
Bot: hi, how are you?
You: what is python
Bot: I don't know the answer. Can you teach me?
Type the answer or 'skip' to skip: A programming language!
Bot: Thank You! I learned a new response!

💰 Crypto Tracker

A real-time cryptocurrency price tracker using the CoinMarketCap API
.

⚙️ Features

Fetches live crypto prices every 60 seconds

Displays selected coins in USD

Easy to extend — just add coin symbols in the list

🗂️ Files
crypto/
│
├── crypto.py
└── api_key.py      # Contains your CoinMarketCap API key

🧾 Example Output
BTC: 67342.23 USD | ETH: 3451.98 USD | BNB: 598.45 USD | SOL: 182.33 USD

🪄 Setup

Get a free API key from CoinMarketCap
.

Create a file named api_key.py in the same folder:

key = "YOUR_API_KEY_HERE"


Run:

python crypto.py

❌⭕ Tic Tac Toe

A simple two-player console game built in Python.
Play alternately as X or O — the first to align three wins!

🧩 Features

Console-based 3x3 grid

Input validation

Win and tie detection

Simple restart and player setup

🗂️ Files
tictactoe/
└── tictactoe.py

▶️ Run
python tictactoe.py

💡 Example Gameplay
My Tic Tac Toe Game
? | ? | ?      1|2|3
? | ? | ?      4|5|6
? | ? | ?      7|8|9
Choose Player (X/O)
Player1: X
Player2: O
Current Player: X
Choose position (1-9): 5
...
X WON!

🧰 Requirements

All projects require Python 3.8+.
For the Crypto Tracker, install the requests library:

pip install requests

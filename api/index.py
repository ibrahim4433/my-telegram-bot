from flask import Flask, request
import telebot
import os
import sys

# Add the parent directory to path so we can import bot.py from the root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bot import bot  # Imports the bot instance from bot.py

app = Flask(__name__)

@app.route('/api/index', methods=['POST'])
def webhook():
    # Standard webhook logic
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        try:
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return ''
        except Exception as e:
            print(f"Error processing update: {e}")
            return 'Error', 500
    else:
        return 'Forbidden', 403

@app.route('/')
def home():
    return "Bot is running! Set the webhook URL now."

if __name__ == "__main__":
    app.run(debug=True)

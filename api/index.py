from flask import Flask, request
import telebot
import os

app = Flask(__name__)

# --- CONFIGURATION ---
# Load the token from Vercel's Environment Variables
TOKEN = os.environ.get('BOT_TOKEN')

# Initialize Bot
# threaded=False is required for Vercel serverless functions
if TOKEN:
    bot = telebot.TeleBot(TOKEN, threaded=False)
else:
    # Fallback to prevent crash if variable is missing (logs error)
    print("ERROR: No BOT_TOKEN found in Environment Variables!", flush=True)
    bot = None

@app.route('/api/index', methods=['POST'])
def webhook():
    # Safety check
    if not bot:
        return 'Bot not configured', 500

    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        return 'Forbidden', 403

# --- BOT COMMANDS ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am secure and running on Vercel!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "I can echo your messages. Just send me text!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "You said: " + message.text)

if __name__ == "__main__":
    app.run(debug=True)

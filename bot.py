import telebot
import os

# 1. Get the Token from the environment (Secure)
TOKEN = os.environ.get('BOT_TOKEN')

# 2. Initialize the Bot
# IMPORTANT: threaded=False is required for Vercel serverless functions
if TOKEN:
    bot = telebot.TeleBot(TOKEN, threaded=False)
else:
    # Fallback to avoid crashing if token is missing (logs error)
    print("ERROR: No BOT_TOKEN found in Environment Variables!")
    # Create a dummy bot to prevent import errors in api/index.py
    bot = telebot.TeleBot("TOKEN_MISSING", threaded=False)

# ---------------------------------------------
# PASTE YOUR BOT CODE BELOW
# ---------------------------------------------

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am a Vercel Telegram Bot Template. Edit bot.py to change me!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "This is a template bot. You can copy-paste your own handlers here.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

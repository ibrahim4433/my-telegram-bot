import telebot
from flask import Flask
from threading import Thread
import os
import time

# --- CONFIGURATION ---
# Replace with your actual token
API_TOKEN = 'YOUR_TOKEN_HERE'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# --- WEB SERVER TO KEEP BOT ALIVE ---
@app.route('/')
def home():
    return "I am alive!"

def run_web_server():
    # Render sets the 'PORT' environment variable automatically.
    # We must listen on this port.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web_server)
    t.start()

# --- BOT COMMANDS ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am running on Render now!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Render says: " + message.text)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # 1. Start the web server in a separate thread
    keep_alive()
    
    # 2. Start the bot
    print("Bot is running...")
    # On Render, we can use standard polling (threading is allowed)
    bot.infinity_polling()

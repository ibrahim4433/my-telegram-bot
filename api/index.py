from flask import Flask, request
import telebot
import os

# 1. Initialize Flask App
app = Flask(__name__)

# 2. Initialize Bot
# We use an environment variable for safety, but you can paste your token directly if testing.
TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_TOKEN_HERE') 
bot = telebot.TeleBot(TOKEN, threaded=False)

# 3. The Webhook Route
# Telegram sends messages to this URL
@app.route('/api/index', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        return 403

# 4. Bot Logic (Your Commands)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello from Vercel! I am serverless now.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "You said: " + message.text)

# 5. Local Testing (Optional)
if __name__ == "__main__":
    app.run(debug=True)

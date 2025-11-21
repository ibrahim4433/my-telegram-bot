from flask import Flask, request
import telebot
import logging

# Initialize Flask
app = Flask(__name__)

# Setup Logging (This enables logs in Vercel)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- CONFIGURATION ---
# Replace this with your actual token
TOKEN = '7629772581:AAEYKPQCRV4RzYRdAQ3H3IJFGzJH7O63isQ'

# Initialize Bot
bot = telebot.TeleBot(TOKEN, threaded=False)

@app.route('/api/index', methods=['POST'])
def webhook():
    # 1. Check if content type is correct
    if request.headers.get('content-type') == 'application/json':
        
        # 2. Get raw data
        json_string = request.get_data().decode('utf-8')
        
        # 3. LOG THE RAW MESSAGE (This will show in Vercel logs)
        print(f"DEBUG: Received Data: {json_string}")

        try:
            # 4. Parse update
            update = telebot.types.Update.de_json(json_string)
            
            # 5. Process update
            bot.process_new_updates([update])
            print("DEBUG: Update processed successfully")
            return ''
        except Exception as e:
            # 6. Catch errors
            print(f"ERROR: Bot failed to process update: {e}")
            return 'Error', 500
    else:
        return 'Forbidden', 403

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("DEBUG: /start command received!")
    try:
        bot.reply_to(message, "It works! I am alive on Vercel.")
        print("DEBUG: Reply sent successfully")
    except Exception as e:
        print(f"ERROR: Could not send reply: {e}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(f"DEBUG: Text received: {message.text}")
    try:
        bot.reply_to(message, "You said: " + message.text)
        print("DEBUG: Reply sent successfully")
    except Exception as e:
        print(f"ERROR: Could not send reply: {e}")

if __name__ == "__main__":
    app.run(debug=True)

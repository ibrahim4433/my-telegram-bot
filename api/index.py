from flask import Flask, request
import telebot
import sys

app = Flask(__name__)

# --- CONFIGURATION ---
# Replace with your REAL token
TOKEN = '7629772581:AAEYKPQCRV4RzYRdAQ3H3IJFGzJH7O63isQ' 

# Initialize Bot
bot = telebot.TeleBot(TOKEN, threaded=False)

@app.route('/api/index', methods=['POST'])
def webhook():
    # 1. FORCE LOG: Prove the function was hit
    print("--- WEBHOOK TRIGGERED ---", flush=True)

    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        
        # 2. FORCE LOG: Show exactly what Telegram sent
        print(f"RAW DATA: {json_string}", flush=True)

        try:
            update = telebot.types.Update.de_json(json_string)
            
            # 3. MANUAL PROCESSING (Bypassing handlers for safety)
            if update.message and update.message.text:
                chat_id = update.message.chat.id
                user_text = update.message.text
                
                print(f"PARSED: Message from {chat_id}: {user_text}", flush=True)
                
                # 4. ATTEMPT TO REPLY
                try:
                    bot.send_message(chat_id, f"I received: {user_text}")
                    print("SUCCESS: Reply sent to Telegram!", flush=True)
                except Exception as e:
                    print(f"ERROR SENDING REPLY: {e}", flush=True)
            else:
                print("INFO: Update received, but it was not a text message.", flush=True)

            return 'OK'
        except Exception as e:
            print(f"CRITICAL ERROR: {e}", flush=True)
            return 'Error', 500
    else:
        print("ERROR: Request was not JSON", flush=True)
        return 'Forbidden', 403

if __name__ == "__main__":
    app.run(debug=True)

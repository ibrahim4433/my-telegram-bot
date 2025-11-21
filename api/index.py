from flask import Flask, request, jsonify
import telebot
import os
import logging

# 1. Setup Logging (This helps you see errors in Vercel logs)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# 2. Fail-Safe Token Loading
# If the token is missing, we won't crash immediately. We'll just log it.
TOKEN = os.environ.get('BOT_TOKEN')
bot = None

if TOKEN:
    try:
        # threaded=False is CRITICAL for Vercel/Serverless
        bot = telebot.TeleBot(TOKEN, threaded=False)
        logger.info("Bot initialized successfully.")
    except Exception as e:
        logger.error(f"Bot failed to start: {e}")
else:
    logger.warning("No BOT_TOKEN found in environment variables!")

# 3. The Webhook Route (Standard Vercel Path)
@app.route('/api/index', methods=['POST'])
def webhook():
    # If bot didn't start, return error but don't crash server
    if not bot:
        return jsonify({"error": "Bot not initialized. Check BOT_TOKEN."}), 500

    try:
        if request.headers.get('content-type') == 'application/json':
            json_string = request.get_data().decode('utf-8')
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return 'OK', 200
        else:
            return 'Forbidden', 403
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        return 'Error', 500

# 4. Health Check Route
# Visit https://your-app.vercel.app/api/index to see if it's alive
@app.route('/api/index', methods=['GET'])
def health_check():
    status = "Running"
    if not TOKEN:
        status = "Running (Warning: No Token)"
    elif not bot:
        status = "Running (Error: Bot Init Failed)"
    
    return jsonify({
        "status": status,
        "platform": "Vercel",
        "token_set": bool(TOKEN)
    })

# 5. Vercel Entry Point
# This 'app' variable is what Vercel looks for
if __name__ == "__main__":
    app.run(debug=True)

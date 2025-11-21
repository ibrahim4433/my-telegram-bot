Vercel Telegram Bot Template (Python)

A one-click template to host a Python Telegram Bot on Vercel for FREE.
No credit card required. No server maintenance.

🚀 Quick Start

1. Deploy to Vercel

Click the button below to fork this repo and deploy it to Vercel automatically.

<!-- REPLACE 'YOUR_GITHUB_USERNAME' and 'YOUR_REPO_NAME' BELOW WITH YOUR ACTUAL DETAILS -->

2. Configure Vercel

Vercel will ask for a BOT_TOKEN. Paste your token from @BotFather.

Wait for the deployment to finish.

Click "Continue to Dashboard".

Visit your new Vercel URL (e.g., https://my-telegram-bot.vercel.app). You should see "Bot is running!".

3. Connect Telegram (Set Webhook)

You must tell Telegram to send messages to your new Vercel app.
Open your web browser and visit this URL (replace the placeholders):

[https://api.telegram.org/botYOUR_BOT_TOKEN/setWebhook?url=https://YOUR_VERCEL_DOMAIN.vercel.app/api/index](https://api.telegram.org/botYOUR_BOT_TOKEN/setWebhook?url=https://YOUR_VERCEL_DOMAIN.vercel.app/api/index)


You should see: {"ok":true, "result":true, "description":"Webhook was set"}.

Done! Your bot is now live 24/7.

🛠 How to Edit the Bot

Go to your GitHub repository (the one Vercel created).

Open bot.py.

Paste your own bot code (handlers, commands, etc).

Commit changes. Vercel will redeploy automatically in seconds.

⚠️ Important Notes

Do not use bot.polling(): Vercel uses webhooks. The template handles this for you.

threaded=False: The bot instance in bot.py must use threaded=False (already set in the template).

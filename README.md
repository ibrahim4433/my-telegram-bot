Vercel Telegram Bot Template (Python)

A one-click template to host a Python Telegram Bot on Vercel for FREE.
No credit card required. No server maintenance.

🚀 Quick Start

Option 1: One-Click Deploy

Click the button below to fork this repo and deploy it to Vercel automatically.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/ibrahim4433/my-telegram-bot&env=BOT_TOKEN&project-name=my-telegram-bot&repository-name=my-telegram-bot)

Important: You must edit this README.md file and replace YOUR_GITHUB_USERNAME and YOUR_REPO_NAME in the link above with your actual GitHub details for this to work!

Option 2: Manual Deploy (If the button fails)

Fork this repository to your own GitHub account.

Go to Vercel.com and log in.

Click "Add New..." -> "Project".

Import the repository you just forked.

In the Environment Variables section, add:

Key: BOT_TOKEN

Value: Your_Telegram_Bot_Token

Click Deploy.

3. Connect Telegram (Set Webhook)

Once deployed, you must tell Telegram where your bot lives.
Open your web browser and visit this URL (replace the placeholders):

[https://api.telegram.org/botYOUR_BOT_TOKEN/setWebhook?url=https://YOUR_VERCEL_DOMAIN.vercel.app/api/index](https://api.telegram.org/botYOUR_BOT_TOKEN/setWebhook?url=https://YOUR_VERCEL_DOMAIN.vercel.app/api/index)


You should see: {"ok":true, "result":true, "description":"Webhook was set"}.

Done! Your bot is now live 24/7.

🛠 How to Edit the Bot

Go to your GitHub repository.

Open bot.py.

Paste your own bot code (handlers, commands, etc).

Commit changes. Vercel will redeploy automatically in seconds.

⚠️ Important Notes

Do not use bot.polling(): Vercel uses webhooks. The template handles this for you.

threaded=False: The bot instance in bot.py must use threaded=False (already set in the template).

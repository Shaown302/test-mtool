import logging
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

from config import BOT_TOKEN, PORT
from commands.start import start
from commands.help import help_cmd
from tools.chatgpt_api import chatgpt
from tools.gemini25 import gemini25
from tools.gemini3 import gemini3
from tools.deepseek import deepseek
from tools.instagram_info import ig
from tools.ff_info import ffinfo

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
application = ApplicationBuilder().token(BOT_TOKEN).build()

# Command Handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_cmd))
application.add_handler(CommandHandler("chatgpt", chatgpt))
application.add_handler(CommandHandler("gemini25", gemini25))
application.add_handler(CommandHandler("gemini3", gemini3))
application.add_handler(CommandHandler("deepseek", deepseek))
application.add_handler(CommandHandler("ig", ig))
application.add_handler(CommandHandler("ffinfo", ffinfo))

@app.route("/")
def home():
    return "Bot Running!"

@app.route("/webhook", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return "ok"

if __name__ == "__main__":
    application.bot.set_webhook(url=f"{application.bot.base_url}/webhook")
    app.run(host="0.0.0.0", port=PORT)

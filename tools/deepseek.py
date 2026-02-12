import requests
from telegram import Update
from telegram.ext import ContextTypes
from core.utils import typing, split_message

async def deepseek(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await typing(update, context)
    if not context.args:
        return await update.message.reply_text("Provide a prompt.")
    prompt = "+".join(context.args)
    url = f"https://void-deep.hosters.club/api/?q={prompt}"
    try:
        r = requests.get(url).text
        for part in split_message(r):
            await update.message.reply_text(f"🚀 DeepSeek 3.2:\n{part}")
    except:
        await update.message.reply_text("API Error.")

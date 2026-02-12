import requests
from telegram import Update
from telegram.ext import ContextTypes
from core.utils import typing, split_message

async def gemini3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await typing(update, context)
    if not context.args:
        return await update.message.reply_text("Provide a prompt.")
    prompt = " ".join(context.args)
    url = f"https://shawon-gemini-3-api.onrender.com/api/ask?prompt={prompt}"
    try:
        r = requests.get(url).json()
        reply = r.get("response", "No response.")
        for part in split_message(reply):
            await update.message.reply_text(f"✨ Gemini 3:\n{part}")
    except:
        await update.message.reply_text("API Error.")

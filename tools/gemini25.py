import requests
from telegram import Update
from telegram.ext import ContextTypes
from core.utils import typing, split_message

async def gemini25(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await typing(update, context)
    if not context.args:
        return await update.message.reply_text("Provide a prompt.")
    prompt = " ".join(context.args)
    url = f"https://gemini-api-flame.vercel.app/?q={prompt}"
    try:
        r = requests.get(url).json()
        reply = r.get("response", "No response.")
        for part in split_message(reply):
            await update.message.reply_text(f"✨ Gemini 2.5:\n{part}")
    except:
        await update.message.reply_text("API Error.")

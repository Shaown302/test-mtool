import requests
from telegram import Update
from telegram.ext import ContextTypes
from core.utils import typing, split_message
from core.database import load_data, save_data

async def chatgpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await typing(update, context)
    if not context.args:
        return await update.message.reply_text("Provide a prompt.")
    prompt = " ".join(context.args)

    user_id = str(update.effective_user.id)
    memory = load_data("memory")
    user_memory = memory.get(user_id, [])
    user_memory.append(f"User: {prompt}")

    url = f"https://addy-chatgpt-api.vercel.app/?text={prompt}"
    try:
        r = requests.get(url).json()
        reply = r.get("reply", "No response.")
        user_memory.append(f"Bot: {reply}")

        memory[user_id] = user_memory[-10:]  # last 10 messages
        save_data("memory", memory)

        for part in split_message(reply):
            await update.message.reply_text(part)
    except:
        await update.message.reply_text("API Error.")

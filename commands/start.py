from telegram import Update
from telegram.ext import ContextTypes
from core.database import load_data, save_data

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users = load_data("users")
    user_id = str(update.effective_user.id)

    if user_id not in users:
        users[user_id] = {"name": update.effective_user.full_name}
        save_data("users", users)

    await update.message.reply_text(
        "🚀 Welcome to MultiTool Bot with AI memory!\n\n"
        "Use /help to see available commands."
    )

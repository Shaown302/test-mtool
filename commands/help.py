from telegram import Update
from telegram.ext import ContextTypes

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📌 Available Commands:\n\n"
        "🤖 AI:\n"
        "/chatgpt <text>\n"
        "/gemini25 <text>\n"
        "/gemini3 <text>\n"
        "/deepseek <text>\n\n"
        "🎮 Gaming:\n"
        "/ffinfo <uid>\n"
        "/emote\n\n"
        "📸 Social:\n"
        "/ig <username>\n"
    )
    await update.message.reply_text(text)

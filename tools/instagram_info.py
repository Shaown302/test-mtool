import requests
from telegram import Update
from telegram.ext import ContextTypes

async def ig(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("Provide username.")
    username = context.args[0]
    url = f"https://instagram-api-ashy.vercel.app/api/ig-profile.php?username={username}"
    try:
        r = requests.get(url).json()
        await update.message.reply_text(
            f"📸 Instagram Profile Info\n\n"
            f"👤 Username: {r.get('username')}\n"
            f"📝 Name: {r.get('full_name')}\n"
            f"👥 Followers: {r.get('followers')}\n"
            f"👤 Following: {r.get('following')}\n"
            f"📸 Posts: {r.get('posts')}\n"
            f"📄 Bio: {r.get('bio')}\n"
            f"🔗 Profile: https://instagram.com/{username}"
        )
    except:
        await update.message.reply_text("API Error.")

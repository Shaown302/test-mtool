import requests
from telegram import Update
from telegram.ext import ContextTypes
from core.utils import typing

async def ffinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await typing(update, context)
    if not context.args:
        return await update.message.reply_text("Provide UID.")
    uid = context.args[0]

    url = f"http://danger-info-alpha.vercel.app/accinfo?uid={uid}&key=DANGERxINFO"
    try:
        data = requests.get(url).json()
        basic = data.get("basicInfo", {})
        clan = data.get("clanBasicInfo", {})
        text = (
            f"🎮 Free Fire Info\n\n"
            f"👤 Nickname: {basic.get('nickname')}\n"
            f"🆔 UID: {basic.get('accountId')}\n"
            f"⭐ Level: {basic.get('level')}\n"
            f"❤️ Likes: {basic.get('liked')}\n"
            f"🌍 Region: {basic.get('region')}\n"
            f"🏆 Rank: {basic.get('rank')}\n\n"
            f"🏰 Clan: {clan.get('clanName')}\n"
            f"👥 Members: {clan.get('memberNum')}"
        )
        await update.message.reply_text(text)
    except:
        await update.message.reply_text("Error fetching info.")

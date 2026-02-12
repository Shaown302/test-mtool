from telegram.constants import ChatAction

async def typing(update, context):
    await context.bot.send_chat_action(update.effective_chat.id, ChatAction.TYPING)

def split_message(text, limit=4000):
    return [text[i:i+limit] for i in range(0, len(text), limit)]

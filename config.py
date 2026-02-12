import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "7333244376"))
PORT = int(os.getenv("PORT", 10000))
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # e.g., https://your-app.onrender.com

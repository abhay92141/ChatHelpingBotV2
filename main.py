from pyrogram import Client
import os

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

app = Client(
    "ChatHelpingBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def start(client, message):
    if message.text == "/start":
        await message.reply_text(
            "👋 Hello!\n\nWelcome to ChatHelpingBot.\nBot is running successfully! 🚀"
        )

app.run()

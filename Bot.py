import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/health')
def health():
    return "OK"

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TARGET_CHAT_ID = 8885363034  # آیدی شما اینجا قرار گرفت
GIF_URL = "https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.mp4"

async def rip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        message_text = " ".join(context.args)
    else:
        message_text = "سلام!"

    try:
        await context.bot.send_message(chat_id=TARGET_CHAT_ID, text=message_text)
        await context.bot.send_animation(chat_id=TARGET_CHAT_ID, animation=GIF_URL)
        await update.message.reply_text("✅ پیام و گیف ارسال شد.")
    except Exception as e:
        await update.message.reply_text(f"❌ خطا: {e}")

def run_bot():
    app_bot = Application.builder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("rip", rip))
    print("Bot started...")
    app_bot.run_polling()

if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)python-telegram-bot
Flask
  

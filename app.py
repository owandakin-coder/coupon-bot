import os
import threading
import time
from flask import Flask
from telegram import Bot
from telegram.ext import Application, CommandHandler

# ===== קונפיגורציה =====
TOKEN = os.environ.get("TELEGRAM_TOKEN")  # נשתמש במשתנה סביבה
if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN environment variable not set")

# ===== אפליקציית Flask לבדיקות בריאות =====
app = Flask(__name__)

@app.route('/')
@app.route('/health')
def health():
    return "OK", 200

# ===== פונקציות הבוט =====
async def start(update, context):
    await update.message.reply_text("ברוך הבא! הבוט רץ.")

def run_bot():
    """הרצת הבוט בנפרד"""
    print("🤖 בוט טלגרם מתחיל...")
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

# ===== הרצה =====
if __name__ == "__main__":
    # הרצת הבוט בת'רד נפרד (רקע)
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()

    # הרצת שרת Flask שאחראי על health checks
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)


import os
import requests
import asyncio
from telegram import Bot
from datetime import datetime

TOKEN = "8214672976:AAF0Vm6fBN5qdNy5DFSK8N3NdXPnTpFA_KI"
CHANNEL_ID = "@getdailydealsil"

# API לדוגמה – Affiliate.com (תצטרך מפתח, אבל יש חינמי)
# בינתיים נשתמש ב-API פתוח של "Real Data" או נדמה נתונים
# כדי שלא תתקע, נשתמש ב-Fake API לבדיקה, ואחר כך נחליף באמיתי.

bot = Bot(token=TOKEN)

def get_coupons():
    """דוגמה סטטית – מייצר כמה קופונים לדוגמה"""
    # כאן יחובר ל-API אמיתי בהמשך
    return [
        {"title": "20% הנחה בשופרסל אונליין", "code": "SAVE20", "link": "https://example.com"},
        {"title": "משלוח חינם באדידס", "code": "FREESHIP", "link": "https://example.com"},
    ]

async def send_coupons():
    coupons = get_coupons()
    for c in coupons:
        text = f"🔥 *{c['title']}*\nקופון: `{c['code']}`\n[השג עכשיו]({c['link']})"
        await bot.send_message(chat_id=CHANNEL_ID, text=text, parse_mode="Markdown")
    print(f"{datetime.now()} – נשלחו {len(coupons)} קופונים")

if __name__ == "__main__":
    asyncio.run(send_coupons())

from telethon import TelegramClient, events
import config  # استيراد القيم من ملف config.py

# إنشاء عميل Telethon باستخدام القيم من config.py
client = TelegramClient("userbot_session", config.API_ID, config.API_HASH)

# الكليشة مع الرابط
response_message = """🔥 شرح مميز حول كيفية الاستخدام 🔥

📌 لمشاهدة الشرح الكامل، اضغط على الرابط أدناه:
🎥 https://youtu.be/h0IIIkfxw30?si=9VKXcKhbBRFKlwoW

✅ تابع الشرح واستمتع!"""

# استماع للرسائل في جميع الدردشات
@client.on(events.NewMessage(pattern=r"^الشرح$"))  # يستجيب فقط عندما تكون الرسالة "الشرح"
async def send_response(event):
    await event.reply(response_message)  # يرد في نفس المحادثة

# تشغيل البوت
client.start()
client.run_until_disconnected()

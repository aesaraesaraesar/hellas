from JoKeRUB import l313l
import sqlite3
import requests

# إعداد قاعدة البيانات
conn = sqlite3.connect('channels.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS channels (id INTEGER PRIMARY KEY, channel_name TEXT, invite_link TEXT)''')
conn.commit()

# تشغيل البوت عبر JoKeRUB
bot = l313l()

@bot.on_message
def handle_message(message):
    user_id = message.from_user.id
    text = message.text
    if "معلومات تيكنوك" in text:
        parts = text.split(" ", 1)
        args = parts[1] if len(parts) > 1 else None
        response = fetch_tiktok_info(args)
        bot.send_message(message.chat.id, response, parse_mode="Markdown")

def fetch_tiktok_info(username):
    if not username:
        return "❌ يرجى إدخال اسم مستخدم تيك توك بعد الأمر."
    api = f"https://tik-batbyte.vercel.app/tiktok?username={username}"
    try:
        response = requests.get(api)
        response.raise_for_status()
        data = response.json()
        return f"*• اسم الحساب:* {data.get('nickname', 'غير معروف')}\n" \
               f"*• المتابعين:* {data.get('followers', 'غير معروف')}\n" \
               f"*• الإعجابات:* {data.get('hearts', 'غير معروف')}\n" \
               f"*• الفيديوهات:* {data.get('videos', 'غير معروف')}\n" \
               f"*• الوصف:* {data.get('bio', 'غير معروف')}\n" \
               f"🔗 [رابط الحساب](https://www.tiktok.com/@{username})"
    except requests.RequestException as e:
        return f"❌ حدث خطأ: {str(e)}"

# تشغيل البوت
bot.run()

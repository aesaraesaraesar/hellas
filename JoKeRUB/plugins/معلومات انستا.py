from telethon import TelegramClient, events
from JoKeRUB import l313l

# اسم الجلسة
client = TelegramClient('bot')

# دالة لجلب معلومات الحساب من إنستغرام باستخدام JoKeRUB
def get_instagram_info_jokerub(username):
    try:
        # جلب معلومات الحساب باستخدام JoKeRUB
        result = l313l(username)
        
        # إذا تم العثور على بيانات الحساب
        if result:
            user_info = f"""
            اسم المستخدم: {result.get('username', 'غير موجود')}
            الاسم الكامل: {result.get('full_name', 'غير موجود')}
            السيرة الذاتية: {result.get('biography', 'غير موجود')}
            المتابعون: {result.get('followers', 'غير موجود')}
            المتابعة: {result.get('following', 'غير موجود')}
            عدد المنشورات: {result.get('posts', 'غير موجود')}
            الحساب خاص: {result.get('is_private', 'غير موجود')}
            الحساب موثق: {result.get('is_verified', 'غير موجود')}
            """
            return user_info
        else:
            return "لم يتم العثور على الحساب أو هناك خطأ في جلب البيانات."
    except Exception as e:
        return f"حدث خطأ: {str(e)}"

# عندما يتلقى البوت رسالة
@client.on(events.NewMessage(pattern=r'\.معلومات انستا (\w+)'))
async def handler(event):
    username = event.pattern_match.group(1)  # الحصول على اسم المستخدم من الرسالة
    result = get_instagram_info_jokerub(username)
    await event.reply(result)  # إرسال الرد للمستخدم


client.start()
client.run_until_disconnected()


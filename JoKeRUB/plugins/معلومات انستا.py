from JoKeRUB import l313l
from telethon import TelegramClient, events
import config  # استيراد الإعدادات من config.py

# إعدادات العميل الخاص بتليجرام باستخدام البيانات من config.py
api_id = config.API_ID
api_hash = config.API_HASH

client = TelegramClient('insta_info_bot', api_id, api_hash)

# دالة لجلب معلومات انستا
async def get_instagram_info(username):
    try:
        # استخدام السورس من JoKeRUB لجلب معلومات الحساب
        user_info = l313l(username)
        
        # جمع المعلومات المطلوبة
        name = user_info.get('name', 'غير متاح')
        bio = user_info.get('bio', 'غير متاح')
        profile_pic = user_info.get('profile_pic', 'غير متاح')
        posts_count = user_info.get('posts', 'غير متاح')
        followers_count = user_info.get('followers', 'غير متاح')
        following_count = user_info.get('following', 'غير متاح')

        # إعداد الرد للمستخدم
        info_message = (
            f"معلومات حساب إنستاجرام لـ {username}:\n\n"
            f"الاسم: {name}\n"
            f"البايو: {bio}\n"
            f"عدد المنشورات: {posts_count}\n"
            f"عدد المتابعين: {followers_count}\n"
            f"عدد الأشخاص الذين يتبعهم: {following_count}\n"
            f"رابط الصورة الشخصية: {profile_pic}"
        )
        return info_message
    except Exception as e:
        return f"حدث خطأ أثناء جلب المعلومات: {str(e)}"

# حدث لتفعيل البوت عند استقبال رسائل
@client.on(events.NewMessage(pattern=r'.معلومات انستا (.+)'))
async def handle_insta_info(event):
    username = event.pattern_match.group(1)  # استخراج اليوزر من الرسالة
    user_info = await get_instagram_info(username)
    
    # إرسال المعلومات للمستخدم
    await event.reply(user_info)

# تشغيل البوت
client.start()
client.run_until_disconnected()

from telethon import events
from JoKeRUB import l313l
import instaloader
import os
import datetime

@l313l.on(events.NewMessage(pattern='\.حساب انستا (.+)'))
async def instagram_scraper(event):
    user = event.pattern_match.group(1)
    
    try:
        L = instaloader.Instaloader()
        
        # تحميل الحساب باستخدام instaloader
        profile = instaloader.Profile.from_username(L.context, user)
        
        # استخراج البيانات
        username = profile.username
        full_name = profile.full_name
        bio = profile.biography
        followers_count = profile.followers
        following_count = profile.followees
        post_count = profile.mediacount
        profile_picture_url = profile.profile_pic_url_hd
        
        # تحميل صورة الملف الشخصي
        avatar_filename = 'avatar.jpg'
        L.download_profilepic(profile)
        
        await event.reply(file=avatar_filename)
        
        response_text = f"""
🔹**معلومات حساب انستجرام**:
🏷 **اسم الحساب**: {full_name}
🏷 **اسم المستخدم**: {username}
👥 **عدد المتابعين**: {followers_count}
🔄 **عدد المتابعين لهم**: {following_count}
🎬 **عدد المنشورات**: {post_count}
📝 **البايو**: {bio}
تم سحب المعلومات بواسطة 𝐒𝐨𝐮𝐫𝐜𝐞 𝐇𝐞𝐥𝐥𝐚s
        """
        
        await event.reply(response_text)
        
        # تنظيف الملف بعد إرساله
        if os.path.exists(avatar_filename):
            os.remove(avatar_filename)
    
    except Exception as e:
        await event.reply(f"❌ حدث خطأ أثناء جلب البيانات: {str(e)}")

l313l.run_until_disconnected()

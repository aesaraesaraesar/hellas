from telethon import events
from JoKeRUB import l313l
import urllib.request
import re
import os
import datetime

@l313l.on(events.NewMessage(pattern='\.معلومات تيك (.+)'))
async def tiktok_scraper(event):
    user = event.pattern_match.group(1)
    url = f'https://www.tiktok.com/@{user}'
    
    try:
        page = urllib.request.urlopen(url)
        content = (page.read()).decode('utf-8')
        
        user_id_match = re.search(r'"id":"(\d+)"', content)
        nickname_match = re.search(r'"nickname":"([^"]+)"', content)
        follower_count_match = re.search(r'"followerCount":(\d+)', content)
        following_count_match = re.search(r'"followingCount":(\d+)', content)
        bio_match = re.search(r'"signature":"([^"]+)"', content)
        video_count_match = re.search(r'"videoCount":(\d+)', content)
        create_time_match = re.search(r'"createTime":(\d+)', content)
        avatar_url_match = re.search(r'"avatarLarger":"([^"]+)"', content)
        
        user_id = user_id_match.group(1) if user_id_match else 'غير متاح'
        nickname = nickname_match.group(1) if nickname_match else 'غير متاح'
        follower_count = follower_count_match.group(1) if follower_count_match else 'غير متاح'
        following_count = following_count_match.group(1) if following_count_match else 'غير متاح'
        bio = bio_match.group(1) if bio_match else 'غير متاح'
        video_count = video_count_match.group(1) if video_count_match else 'غير متاح'

        # تحويل create_time إلى تاريخ قابل للقراءة
        create_time_timestamp = int(create_time_match.group(1)) / 1000 if create_time_match else None
        create_time = datetime.datetime.utcfromtimestamp(create_time_timestamp).strftime('%Y-%m-%d %H:%M:%S') if create_time_timestamp else 'غير متاح'

        avatar_url = avatar_url_match.group(1).replace(r'\u002F', '/') if avatar_url_match else 'غير متاح'
        
        # تحميل صورة الملف الشخصي
        avatar_filename = 'avatar.jpg'
        urllib.request.urlretrieve(avatar_url, avatar_filename)
        await event.reply(file=avatar_filename)
        
        response = f"""
        🔹 **معلومات الحساب:**
        🏷 **اسم الحساب:** {nickname}
        🆔 **User ID:** {user_id}
        👥 **المتابعين:** {follower_count}
        🔄 **المتابعهم:** {following_count}
        🎬 **عدد الفيديوهات:** {video_count}
        📅 **تاريخ الإنشاء:** {create_time}
        📝 **البايو:** {bio}
        """
        
        await event.reply(response)
    except Exception as e:
        await event.reply(f"❌ حدث خطأ أثناء جلب البيانات: {str(e)}")

l313l.run_until_disconnected()




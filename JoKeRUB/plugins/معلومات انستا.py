from telethon import events
from JoKeRUB import l313l
import requests
import re
from bs4 import BeautifulSoup
import os
import datetime

@l313l.on(events.NewMessage(pattern='\.حساب انستجرام (.+)'))
async def instagram_scraper(event):
    user = event.pattern_match.group(1)
    url = f'https://www.instagram.com/{user}/'
    
    try:
        # إرسال طلب GET للحصول على محتويات الصفحة
        response = requests.get(url)
        
        # إذا كانت الصفحة تحتوي على بيانات 200
        if response.status_code == 200:
            content = response.text
            soup = BeautifulSoup(content, 'html.parser')
            
            # استخراج البيانات من JSON المدمج في الصفحة
            json_data_match = re.search(r'window\._sharedData = ({.*?});</script>', content)
            if not json_data_match:
                await event.reply("❌ حدث خطأ أثناء استخراج بيانات الحساب.")
                return
            
            json_data = json_data_match.group(1)
            
            # تحويل البيانات إلى Python dict
            import json
            data = json.loads(json_data)
            user_data = data['entry_data']['ProfilePage'][0]['graphql']['user']
            
            username = user_data['username']
            full_name = user_data['full_name']
            bio = user_data['biography']
            followers_count = user_data['edge_followed_by']['count']
            following_count = user_data['edge_follow']['count']
            post_count = user_data['edge_owner_to_timeline_media']['count']
            profile_picture_url = user_data['profile_pic_url_hd']
            account_creation_timestamp = user_data['date_joined']
            
            # تحويل تاريخ الإنشاء إلى تنسيق مقروء
            create_time = datetime.datetime.utcfromtimestamp(account_creation_timestamp).strftime('%Y-%m-%d %H:%M:%S')
            
            # تحميل صورة الملف الشخصي
            avatar_filename = 'avatar.jpg'
            img_response = requests.get(profile_picture_url)
            with open(avatar_filename, 'wb') as f:
                f.write(img_response.content)
            
            await event.reply(file=avatar_filename)
            
            response_text = f"""
🔹**معلومات حساب انستجرام**:
🏷 **اسم الحساب**: {full_name}
🏷 **اسم المستخدم**: {username}
👥 **عدد المتابعين**: {followers_count}
🔄 **عدد المتابعين لهم**: {following_count}
🎬 **عدد المنشورات**: {post_count}
📝 **البايو**: {bio}
📅 **تاريخ الانضمام**: {create_time}
تم سحب المعلومات بواسطة 𝐒𝐨𝐮𝐫𝐜𝐞 𝐇𝐞𝐥𝐥𝐚s
            """
            
            await event.reply(response_text)
            
            # تنظيف الملف بعد إرساله
            if os.path.exists(avatar_filename):
                os.remove(avatar_filename)
        
        else:
            await event.reply("❌ حدث خطأ في الاتصال بالإنستجرام.")
    
    except Exception as e:
        await event.reply(f"❌ حدث خطأ أثناء جلب البيانات: {str(e)}")

l313l.run_until_disconnected()


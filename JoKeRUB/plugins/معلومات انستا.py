import requests
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from JoKeRUB import l313l

@l313l.on("حساب انستا")
async def inst(event):
    # استخراج اليوزر من الأمر
    args = event.text.split("+")
    if len(args) < 2:
        return await event.reply("❌ يرجى إدخال اسم المستخدم بعد الأمر، مثال:\n.حساب انستا +username")
    
    username = args[1].strip()
    
    headers = {
        'accept': '*/*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
        ]),
        'x-asbd-id': '129477',
        'x-csrftoken': 'mFcLz5S7aKKvWLBOWjTVqtpJAGYmjgqg',
        'x-ig-app-id': '936619743392459',
        'x-requested-with': 'XMLHttpRequest',
    }

    api = 'https://www.instagram.com/api/v1/users/web_profile_info/'
    try:
        response = requests.get(api, headers=headers, params={'username': username})
        response.raise_for_status()
        data = response.json().get('data', {}).get('user', {})

        if not data:
            return await event.reply(f"❌ لم يتم العثور على معلومات للحساب: {username}")
        
        # استخراج المعلومات
        bio_links = ""
        for link in data.get('bio_links', []):
            if link.get('title', '').lower() != "الملف الشخصي على فيسبوك":
                bio_links += f"\n🔗 {link.get('title', ' ')} ↢ [اضغط هنا]({link.get('url', ' ')})"
        
        caption = f"""
• اسم الحساب ↢「{data.get('full_name', 'N/A')}」
• يوزر الحساب ↢「{data.get('username', 'N/A')}」
• المتابعين ↢「{data.get('edge_followed_by', {}).get('count', 0)}」
• الي يتابعهم ↢「{data.get('edge_follow', {}).get('count', 0)}」
• ايدي الحساب ↢「{data.get('id', 'N/A')}」
• فئة الحساب ↢「{data.get('category_name', 'ما بعرف')}」
• الحساب موثق ↢「{"نعم" if data.get('is_verified', False) else "لا"}」
• الحساب خاص ↢「{"نعم" if data.get('is_private', False) else "لا"}」
• عدد المنشورات ↢「{data.get('edge_owner_to_timeline_media', {}).get('count', 0)}」
• حساب الفيسبوك ↢「[{data.get('fb_profile_biolink', {}).get('name', ' ')}]({data.get('fb_profile_biolink', {}).get('url', ' ')})」
• الوصف ↢「{data.get('biography', 'N/A')}」
{bio_links}
"""

        await event.reply_photo(
            data.get('profile_pic_url_hd', ''),
            caption=caption,
            parse_mode="Markdown"
        )
    
    except requests.RequestException as e:
        await event.reply(f"❌ خطأ أثناء جلب البيانات: {str(e)}")



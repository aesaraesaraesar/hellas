import requests
import random
from JoKeRUB import l313l

@l313l.on("حساب انستا")
async def inst(event):
    args = event.text.split("+", 1)
    if len(args) < 2:
        return await event.reply("❌ يرجى إدخال اسم المستخدم بعد الأمر، مثال:\n.حساب انستا +username")
    
    username = args[1].strip()
    
    headers = {
        'accept': '*/*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': random.choice([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, مثل Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, مثل Gecko) Version/14.0.1 Safari/605.1.15',
        ]),
        'x-ig-app-id': '936619743392459',
        'x-requested-with': 'XMLHttpRequest',
    }

    api = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}'
    
    try:
        response = requests.get(api, headers=headers)
        response.raise_for_status()
        data = response.json().get('data', {}).get('user', {})

        if not data:
            return await event.reply(f"❌ لم يتم العثور على معلومات للحساب: {username}")
        
        # استخراج المعلومات
        full_name = data.get('full_name', 'N/A')
        followers = data.get('edge_followed_by', {}).get('count', 0)
        following = data.get('edge_follow', {}).get('count', 0)
        user_id = data.get('id', 'N/A')
        category = data.get('category_name', 'غير محدد')
        is_verified = "✅ نعم" if data.get('is_verified', False) else "❌ لا"
        is_private = "🔒 نعم" if data.get('is_private', False) else "🔓 لا"
        posts = data.get('edge_owner_to_timeline_media', {}).get('count', 0)
        biography = data.get('biography', 'N/A')
        profile_pic = data.get('profile_pic_url_hd', '')

        # استخراج روابط إضافية (إن وجدت)
        links_text = ""
        for link in data.get('bio_links', []):
            title = link.get('title', 'رابط إضافي')
            url = link.get('url', '#')
            links_text += f"\n🔗 {title} ➝ [اضغط هنا]({url})"

        caption = f"""
📌 **معلومات حساب انستجرام**
👤 **الاسم:** {full_name}
🔗 **المعرف:** @{username}
👥 **المتابعين:** {followers}
🚀 **يتابع:** {following}
🆔 **معرف الحساب:** {user_id}
🏷️ **الفئة:** {category}
✅ **موثق:** {is_verified}
🔒 **خاص:** {is_private}
📸 **عدد المنشورات:** {posts}
📝 **الوصف:** {biography}
{links_text}
"""

        await event.reply_photo(profile_pic, caption=caption, parse_mode="Markdown")
    
    except requests.RequestException as e:
        await event.reply(f"❌ حدث خطأ أثناء جلب البيانات: {str(e)}")


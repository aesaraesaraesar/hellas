from JoKeRUB import l313l
import requests
import random

# دالة لاختيار User-Agent عشوائي
def asasa():
    ase = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
    ]
    return random.choice(ase)

# دالة لجلب معلومات حساب انستجرام
def get_instagram_info(username):
    headers = {
        'accept': '*/*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': asasa(),
        'x-asbd-id': '129477',
        'x-csrftoken': 'mFcLz5S7aKKvWLBOWjTVqtpJAGYmjgqg',
        'x-ig-app-id': '936619743392459',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'username': username,
    }

    api = 'https://www.instagram.com/api/v1/users/web_profile_info/'
    response = requests.get(api, headers=headers, params=params)

    if response.status_code != 200:
        return None  # يعني أنه لم يتم العثور على الحساب أو حدوث خطأ

    data = response.json().get('data', {}).get('user', {})
    if not data:
        return None

    return {
        "full_name": data.get('full_name', 'N/A'),
        "username": data.get('username', 'N/A'),
        "followers": data.get('edge_followed_by', {}).get('count', 0),
        "following": data.get('edge_follow', {}).get('count', 0),
        "biography": data.get('biography', 'N/A'),
        "id": data.get('id', 'N/A'),
        "category": data.get('category_name', 'N/A'),
        "verified": "نعم" if data.get('is_verified', False) else "لا",
        "private": "نعم" if data.get('is_private', False) else "لا",
        "posts": data.get('edge_owner_to_timeline_media', {}).get('count', 0),
        "profile_pic_url": data.get('profile_pic_url_hd', ''),
    }

# دالة لمعالجة الأمر واستخراج المعلومات
@l313l.on("معلومات انستا")
def instagram_info(msg):
    try:
        username = msg.text.split(' ')[1].strip()  # استخراج اسم المستخدم من الرسالة

        # جلب البيانات من API
        account_info = get_instagram_info(username)

        if not account_info:
            msg.reply(f"لم يتم العثور على معلومات للحساب: {username}")
            return

        # إنشاء الرسالة التي ستعرض المعلومات
        caption = f"""
• اسم الحساب ↢「{account_info['full_name']}」
• يوزر الحساب ↢「{account_info['username']}」
• المتابعين ↢「{account_info['followers']}」
• الي يتابعهم ↢「{account_info['following']}」
• ايدي الحساب ↢「{account_info['id']}」
• فئة الحساب ↢「{account_info['category']}」
• الحساب موثق ↢「{account_info['verified']}」
• الحساب خاص ↢「{account_info['private']}」
• عدد المنشورات ↢「{account_info['posts']}」
• الوصف ↢「{account_info['biography']}」
"""

        # إرسال صورة بروفايل الحساب
        msg.reply_photo(account_info['profile_pic_url'], caption=caption)

    except Exception as e:
        msg.reply(f"حدث خطأ: {str(e)}")


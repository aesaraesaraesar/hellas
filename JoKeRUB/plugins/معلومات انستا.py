from JoKeRUB import l313l
import requests
import base64
import logging
import random

def get_instagram_info(username):
    """جلب معلومات الحساب من إنستاجرام"""
    try:
        tomy = f"-1::{username}"
        tom = base64.b64encode(tomy.encode()).decode()
        headers = {
            'user-agent': asasa()
        }
        url = f"https://instanavigation.net/api/v1/stories/{tom}"
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            logging.error(f"Error fetching Instagram info: {response.text}")
            return None

        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        return None

def asasa():
    ase = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
    ]
    return random.choice(ase)

def handle_message(event):
    """معالجة الرسالة القادمة"""
    chat_id = event.chat_id
    text = event.text.strip()
    sender_id = event.sender_id
    
    logging.debug(f"Received message: {text} from ID: {sender_id}")
    
    if text.startswith('.معلومات انستا'):
        parts = text.split()
        if len(parts) < 2:
            l313l.send_message(chat_id, "⚠️ يرجى إدخال اسم المستخدم بعد الأمر.")
            return
        
        username = parts[1]
        fetch_instagram_info(chat_id, username)

def fetch_instagram_info(chat_id, username):
    instagram_info = get_instagram_info(username)
    
    if not instagram_info:
        l313l.send_message(chat_id, "⚠️ حدث خطأ أثناء جلب المعلومات. حاول لاحقًا.")
        return
    
    user_info = instagram_info.get('user_info', {})
    if not user_info:
        l313l.send_message(chat_id, f"❌ لم يتم العثور على معلومات للحساب *{username}*، تأكد من صحة المعرف.")
        return
    
    full_name = user_info.get('full_name', 'غير متوفر')
    is_private = 'نعم' if user_info.get('is_private', False) else 'لا'
    media_count = user_info.get('posts', 'غير متوفر')
    followers = user_info.get('followers', 'غير متوفر')
    following = user_info.get('following', 'غير متوفر')
    bio = user_info.get('biography', 'غير متوفر')
    profile_pic = user_info.get('profile_pic_url', '')
    is_verified = 'نعم' if user_info.get('is_verified', False) else 'لا'

    message = (f"*⚡ اسم الحساب: {full_name}\n"
               f"📛 يوزر الحساب: @{username}\n"
               f"👥 المتابعين: {followers}\n"
               f"🚀 المتابعين له: {following}\n"
               f"📌 معرف الحساب: {user_info.get('id', 'غير متوفر')}\n"
               f"🔒 الحساب خاص: {is_private}\n"
               f"✅ الحساب موثق: {is_verified}\n"
               f"🖼 عدد المنشورات: {media_count}\n"
               f"📄 السيرة الذاتية: {bio}*")
    
    if profile_pic:
        l313l.send_photo(chat_id, profile_pic, caption=message, parse_mode='Markdown')
    else:
        l313l.send_message(chat_id, message, parse_mode='Markdown')

l313l.run(handle_message)

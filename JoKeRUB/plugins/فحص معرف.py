from JoKeRUB import l313l
from JoKeRUB.core.logger import logging
import re
from telethon import events

# دالة لفحص اليوزر إذا كان متعلقًا بـ NFT
def check_nft_status(username):
    try:
        user = l313l.get_user(username)  # جلب بيانات المستخدم من سورس JoKeRUB
        if not user:
            return f"❌ المستخدم @{username} غير موجود."

        bio = user.get("about", "")
        name = f"{user.get('first_name', '')} {user.get('last_name', '')}".strip()
        
        nft_keywords = ["NFT", "Crypto", "Web3", "Ethereum", "Blockchain", "DeFi"]

        for keyword in nft_keywords:
            if re.search(rf"\b{keyword}\b", bio, re.IGNORECASE) or re.search(rf"\b{keyword}\b", name, re.IGNORECASE):
                return f"✅ الحساب @{username} متعلق بـ NFT."

        return f"❌ الحساب @{username} لا يبدو متعلقًا بـ NFT."
    
    except Exception as e:
        logging.error(f"حدث خطأ: {e}")
        return "❌ حدث خطأ أثناء الفحص."

# حدث يستمع للرسائل التي تحتوي على معرف مثل @username
@l313l.on(events.NewMessage())
async def handler(event):
    if event.is_private:  # تجنب الرد في الخاص إذا كنت لا تريده
        return

    message = event.raw_text.strip()  # جلب نص الرسالة
    match = re.search(r'@(\w+)', message)  # البحث عن يوزر في الرسالة

    if match:
        username = match.group(1)  # استخراج اليوزر من الرسالة
        result = check_nft_status(username)  # فحص اليوزر
        await event.reply(result)  # الرد على نفس الرسالة

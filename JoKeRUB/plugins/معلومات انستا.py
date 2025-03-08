from JoKeRUB import l313l
import requests

@l313l.on_message(filters.text & filters.private)
async def instagram_info(client, message):
    if message.text.startswith('.معلومات انستا'):
        username = message.text.split(' ')[1]  # استخرج اسم المستخدم من الرسالة

        headers = {
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'x-requested-with': 'XMLHttpRequest',
        }
        
        api_url = f"https://www.instagram.com/{username}/?__a=1"
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            user_data = data.get('graphql', {}).get('user', {})
            if user_data:
                full_name = user_data.get('full_name', 'غير معروف')
                username = user_data.get('username', 'غير معروف')
                followers = user_data.get('edge_followed_by', {}).get('count', 0)
                following = user_data.get('edge_follow', {}).get('count', 0)
                bio = user_data.get('biography', 'لا توجد معلومات')

                # إعداد النص لعرضه
                user_info = f"""
                • اسم الحساب: {full_name}
                • يوزر الحساب: {username}
                • المتابعين: {followers}
                • المتابعين لهم: {following}
                • الوصف: {bio}
                """
                await message.reply(user_info)
            else:
                await message.reply(f"لم يتم العثور على معلومات للحساب {username}.")
        else:
            await message.reply("حدث خطأ أثناء جلب البيانات من Instagram.")

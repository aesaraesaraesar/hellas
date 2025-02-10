import random
import os
import time
import requests
from JoKeRUB import l313l

time2 = time.strftime('%d/%m/%Y')

E = '\033[1;31m'
Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
C = "\033[2;35m"
B = '\033[2;36m'
Y = '\033[1;34m'
M = '\x1b[1;37m'

Good = 0
bad = 0

try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')

output = render('SYYAD', colors=['white', 'red'], align='center')
print(output)
print('\n')
print(f'{X}▭▬▭'*20)

# إزالة التوكن من الإدخال اليدوي
# التوكن يجب أن يتم تخزينه بطريقة آمنة، أو إضافته من خلال بيئة البيئة
token = "توكن_البوت"  # استبدل هنا بالتوكن الفعلي للبوت
iD = "رقم_الدردشة_الخاص_بك"  # استبدل هنا بالـ ID الخاص بك في تيليجرام

print(f'{F}▭▬▭'*20)

while True:
    try:
        # الانتظار لإدخال الأمر من المستخدم
        command = input(f"{Z}[{Z}?{Z}]{Z} أدخل الأمر (مثال: .صيد تيكنوك): ")

        if command == ".صيد تيكنوك":
            # توليد أسماء مستخدمين عشوائية (الرباعية)
            y = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm') for _ in range(1))
            j = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm') for _ in range(1))
            w = ''.join(random.choice('qwertyuipoasdfghjklzxcvbnm') for _ in range(1))
            v = ''.join(random.choice('qwertyuipoasdfghjklzxcvbnm') for _ in range(1))

            user = y + w + j + v  # اسم مستخدم عشوائي من 4 حروف

            headers = {
                "Host": "www.tiktok.com",
                "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": "\"Android\"",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "sec-fetch-site": "none",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "accept-language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr;q=0.6,hu;q=0.5,zh-CN;q=0.4,zh;q=0.3"
            }

            response = requests.get(f'https://www.tiktok.com/@{user}', headers=headers)
            tikinfo = response.text

            # استخراج معلومات الحساب
            getting = tikinfo.split('webapp.user-detail"')[1].split('"RecommendUserList"')[0]
            user_id = getting.split('id":"')[1].split('",')[0]
            followers = getting.split('followerCount":')[1].split(',"')[0]
            following = getting.split('followingCount":')[1].split(',"')[0]

            bad += 1

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''
{X}---------------------------------------------------
- {F} Good User Tik : {Good}
- {Z} Bad User Tik : {bad}
- {B} Check User Tik : {user}
- {M} Dev : @BBBBYB1
{X}---------------------------------------------------
''')

        else:
            print(f"{Z}[{Z}?{Z}]{Z} صيغة الإدخال غير صحيحة، يجب أن تكون .صيد تيكنوك فقط")

    except (KeyError, IndexError):
        Good += 1
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'''
{X}---------------------------------------------------
- {F} Good User Tik : {Good}
- {Z} Bad User Tik : {bad}
- {B} Check User Tik : {user}
{X}---------------------------------------------------
''')

        SE = f'''
DONE USER TIK IS BEST⚡
- - - - - - - - - - - - - - - - - - - - - - - - - 
- user  : ❲ {user} ❳
- TRUE : ❲ {Good} ❳
- TIME : {time2}
- - - - - - - - - - - - - - - - - - - - - - - - 
py(@BBBBYB1)(@ss_yj7)'''

        requests.post(f"https://api.telegram.org/bot{token}/sendvideo?chat_id={iD}&video=https://t.me/m_6_yy/93&caption={SE}")


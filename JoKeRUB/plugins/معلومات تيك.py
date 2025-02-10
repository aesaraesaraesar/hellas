from ms4 import InfoTik
from JoKeRUB import l313l

def get_tiktok_info(command):
    try:
        # التحقق من صيغة الأمر
        if command.startswith(".معلومات تيك توك +"):
            username = command.replace(".معلومات تيك توك +", "").strip()
            
            # استخدام InfoTik للحصول على معلومات الحساب
            user_info = InfoTik(username)

            # استخدام l313l من JoKeRUB لإظهار المزيد من المعلومات أو للتعامل مع البيانات
            additional_info = l313l(user_info)

            # طباعة معلومات الحساب
            print("معلومات الحساب:")
            print(f"الاسم: {user_info['name']}")
            print(f"عدد المتابعين: {user_info['followers_count']}")
            print(f"عدد الإعجابات: {user_info['likes_count']}")
            print(f"التفاعل: {user_info['engagement']}")
            print(f"الفيديوهات المنشورة: {user_info['video_count']}")
            print(f"بيانات إضافية: {additional_info}")
        else:
            print("الصيغة غير صحيحة، يجب أن تبدأ بـ .معلومات تيك توك + [اسم المستخدم]")

    except Exception as e:
        print(f"حدث خطأ أثناء جلب المعلومات: {str(e)}")

# مثال على الاستخدام
command = input("أدخل الأمر بصيغة '.معلومات تيك توك + اليوزر': ")
get_tiktok_info(command)

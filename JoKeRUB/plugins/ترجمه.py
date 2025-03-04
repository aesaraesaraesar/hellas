from JoKeRUB import l313l
from googletrans import Translator

bot = l313l()
translator = Translator()

languages = {
    "ar": "العربية", "en": "الإنكليزية", "fr": "الفرنسية", "ru": "الروسية",
    "tr": "التركية", "pt": "البرتغالية", "hi": "الهندية", "is": "الأيسلندية",
    "ja": "اليابانية", "ko": "الكورية", "zh-cn": "الصينية", "it": "الإيطالية",
    "de": "الألمانية", "ro": "الرومانية", "uk": "الأوكرانية", "ca": "الكاتالونية",
    "sr": "الصربية", "hr": "الكرواتية", "no": "النرويجية", "af": "الأفريقية",
    "sq": "الألبانية", "vi": "الفيتنامية", "pa": "البنجابية", "ne": "النيبالية",
    "ky": "القيرغيزية", "ku": "الكردية (الكرمانجية)", "cs": "التشيكية",
    "ms": "الماليزية", "ml": "المالايالامية"
}

@bot.on_message(".انواع الترجمه")
def send_translation_types(message):
    lang_list = "\n".join([f"{code} - {name}" for code, name in languages.items()])
    bot.reply(message, f"\n**🔹 اللغات المدعومة:**\n{lang_list}")

@bot.on_message(".ترجمه", reply=True)
def translate_message(message):
    try:
        if not message.reply_to_message or not message.reply_to_message.text:
            return bot.reply(message, "⚠️ يجب الرد على رسالة تحتوي على نص.")
        
        parts = message.text.split()
        if len(parts) < 2:
            return bot.reply(message, "⚠️ يجب تحديد اللغة. استخدم `.انواع الترجمه` لمعرفة اللغات المدعومة.")
        
        target_lang = parts[1]
        if target_lang not in languages:
            return bot.reply(message, "⚠️ اللغة غير مدعومة. استخدم `.انواع الترجمه` لمعرفة اللغات المدعومة.")
        
        translated_text = translator.translate(message.reply_to_message.text, dest=target_lang).text
        bot.reply(message, f"**🔹 الترجمة إلى {languages[target_lang]}:**\n{translated_text}")
    except Exception as e:
        bot.reply(message, f"⚠️ حدث خطأ: {str(e)}")

print("✅ البوت يعمل بنجاح بدون توكن!")
bot.run()

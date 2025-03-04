from JoKeRUB import l313l  # تأكد من أنك قد قمت بتثبيت واعداد مكتبة JoKeRUB
from telebot import types
from googletrans import Translator

translator = Translator()
source_language = None

# قائمة اللغات
languages = {
    'ar': 'العربية',
    'en': 'الإنكليزية',
    'fr': 'الفرنسية',
    'ru': 'الروسية',
    'tr': 'التركية',
    'pt': 'البرتغالية',
    'hi': 'الهندية',
    'is': 'الأيسلندية',
    'ja': 'اليابانية',
    'ko': 'الكورية',
    'zh-cn': 'صيني',
    'it': 'إيطالي',
    'de': 'ألماني',
    'ro': 'روماني',
    'uk': 'أوكراني',
    'ca': 'كاتالوني',
    'sr': 'صربي',
    'hr': 'كرواتي',
    'no': 'نرويجي',
    'af': 'أفريقي',
    'sq': 'ألباني',
    'vi': 'فيتنامي',
    'pa': 'بنجابي',
    'ne': 'نيبالي',
    'ky': 'قيرغيزستان',
    'ku': 'كردي (كرمانجي)',
    'cs': 'تشيكي',
    'ml': 'مالايالامية',
    'ms': 'ماليزيا'
}

# عند بدء المحادثة
@l313l.command("انواع الرتجمه")
def show_translation_types(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(f"{lang}", callback_data=lang) for lang in languages.values()]
    markup.add(*buttons)
    message.reply("اختر اللغة التي تريد الترجمة إليها:", reply_markup=markup)

# عند اختيار اللغة
@l313l.callback_query_handler(func=lambda call: True)
def handle_language_selection(call):
    global source_language
    source_language = call.data

    if source_language in languages:
        response = f"اللغة المختارة هي: {languages[source_language]}. الآن أرسل النص الذي تريد ترجمته."
        l313l.send_message(call.message.chat.id, response)
        l313l.delete_message(call.message.chat.id, call.message.message_id)

# عند كتابة النص مع أمر ".ترجمه"
@l313l.message_handler(func=lambda message: message.text.startswith(".ترجمه"))
def handle_translation_request(message):
    global source_language
    if not source_language:
        l313l.send_message(message.chat.id, "لم تقم باختيار اللغة بعد. استخدم .انواع الرتجمه لاختيار اللغة.")
        return

    parts = message.text.split(" ", 2)
    if len(parts) < 3:
        l313l.send_message(message.chat.id, "استخدم الأمر بصيغة: .ترجمه <اللغة> <الرد على الرسالة>")
        return

    target_language = parts[1]
    if target_language not in languages:
        l313l.send_message(message.chat.id, "اللغة غير مدعومة. من فضلك اختر لغة صحيحة.")
        return

    # الحصول على الرد على الرسالة
    reply_message = message.reply_to_message
    if not reply_message:
        l313l.send_message(message.chat.id, "من فضلك رد على رسالة أخرى لاستخدامها في الترجمة.")
        return

    # ترجمة النص
    source_text = reply_message.text
    translation = translator.translate(source_text, dest=target_language)
    translated_text = translation.text
    
    l313l.send_message(message.chat.id, translated_text)

# بدء البوت
print("🖤 لا تيأس حاول حتى يعمل 🖤")
l313l.run_polling()

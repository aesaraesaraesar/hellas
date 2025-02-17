import re
from telethon import events, types
from JoKeRUB.helpers.functions.functions import translate
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete, edit_or_reply

# ✅ قائمة اللغات المدعومة
langs = {
    'عربي': 'ar', 'انجليزي': 'en', 'فرنسي': 'fr', 'تركي': 'tr', 'اسباني': 'es', 'الماني': 'de',
    'ايطالي': 'it', 'هندي': 'hi', 'صيني': 'zh', 'روسي': 'ru', 'ياباني': 'ja', 'كردي': 'ku'
}

# ✅ دالة الترجمة مع تصحيح الأخطاء
async def gtrans(text, lan):
    try:
        if lan not in langs.values():
            return f"⚠️ اللغة `{lan}` غير مدعومة! استخدم رمز لغة صحيح."
        
        response = translate(text, lang_tgt=lan)
        if response == 400:
            return "❌ حدث خطأ أثناء الترجمة!"
        return response
    except Exception as er:
        return f"❌ خطأ في الترجمة: {er}"

# ✅ أمر الترجمة يدويًا
@l313l.ar_cmd(pattern="ترجمة(?:\s+(\w{2,}))?")
async def translate_text(event):
    input_str = event.pattern_match.group(1)  # استخراج رمز اللغة

    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "ar"  # الافتراضي: عربي
    elif input_str and ";" in input_str:
        lan, text = input_str.split(";", 1)
    else:
        return await edit_delete(event, "**📝 استخدم `.ترجمة en` أو `.ترجمة ar` أو رد على رسالة**", time=5)

    text, lan = text.strip(), lan.strip()

    if len(text) < 2:
        return await edit_delete(event, "⚠️ النص قصير جدًا!")

    trans = await gtrans(text, lan)
    if "⚠️" in trans or "❌" in trans:
        return await edit_delete(event, trans)

    output_str = f"**✅ تمت الترجمة إلى `{lan}`:**\n`{trans}`"
    await edit_or_reply(event, output_str)

# ✅ تفعيل وتعطيل الترجمة الفورية
@l313l.ar_cmd(pattern="الترجمة الفورية")
async def enable_auto_translate(event):
    addgvar("transnow", "True")
    await edit_delete(event, "**✅ تم تفعيل الترجمة الفورية**")

@l313l.ar_cmd(pattern="ايقاف الترجمة")
async def disable_auto_translate(event):
    delgvar("transnow")
    await edit_delete(event, "**❌ تم تعطيل الترجمة الفورية**")

# ✅ تغيير لغة الترجمة الفورية
@l313l.ar_cmd(pattern="لغة الترجمة (\w+)")
async def change_auto_translate_lang(event):
    lang = event.pattern_match.group(1).strip().lower()
    if lang in langs:
        lang_code = langs[lang]
        addgvar("translang", lang_code)
        await edit_delete(event, f"**✅ تم تغيير لغة الترجمة الفورية إلى `{lang}` ({lang_code})**")
    else:
        await edit_delete(event, "⚠️ اللغة غير مدعومة! استخدم لغة صحيحة.")

# ✅ الترجمة الفورية للرسائل الصادرة
@l313l.on(events.NewMessage(outgoing=True))
async def auto_translate(event):
    if gvarstatus("transnow"):
        if event.media:
            return  # لا تترجم إذا كانت الرسالة تحتوي على صور أو وسائط
        text = event.message.message.strip()
        translated_message = await gtrans(text, gvarstatus("translang") or "ar")
        if translated_message and "⚠️" not in translated_message and "❌" not in translated_message:
            await event.message.edit(translated_message)

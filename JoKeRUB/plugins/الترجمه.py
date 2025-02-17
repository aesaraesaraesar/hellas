import re
from asyncio import sleep
from telethon import events, types
from JoKeRUB.helpers.functions.functions import translate
from JoKeRUB import l313l
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete, edit_or_reply

langs = {
    'عربي': 'ar', 'فارسي': 'fa', 'بلغاري': 'bg', 'صيني مبسط': 'zh', 'صيني تقليدي': 'zh-TW',
    'كرواتي': 'hr', 'دنماركي': 'da', 'ألماني': 'de', 'إنجليزي': 'en', 'فنلندي': 'fil',
    'فرنسي': 'fr', 'يوناني': 'el', 'هنغاري': 'hu', 'كوري': 'ko', 'إيطالي': 'it',
    'ياباني': 'ja', 'نرويجي': 'no', 'بولندي': 'pl', 'برتغالي': 'pt', 'روسي': 'ru',
    'سلوفيني': 'sl', 'إسباني': 'es', 'سويدي': 'sv', 'تركي': 'tr', 'هندي': 'ur', 'كردي': 'ku',
}

def soft_deEmojify(text):
    return re.sub(r'[^\x00-\x7F]+', '', text)

async def gtrans(text, lan):
    try:
        response = translate(text, lang_tgt=lan)
        if response == 400:
            return False
    except Exception as er:
        return f"حدث خطأ \n{er}"
    return response

@l313l.ar_cmd(pattern="ترجمة(?:\s+(\w{2,}))?")
async def _(event):
    input_str = event.pattern_match.group(1)  # يلتقط اللغة إذا وُجدت

    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "ar"  # إذا لم يتم تحديد لغة، ستكون الافتراضية "ar"
    elif input_str and ";" in input_str:
        lan, text = input_str.split(";", 1)  # تقسيم اللغة والنص
    else:
        return await edit_delete(event, "**قم بالرد على الرسالة أو أدخل النص للترجمة**", time=5)

    text = soft_deEmojify(text.strip())
    lan = lan.strip()

    if len(text) < 2:
        return await edit_delete(event, "قم بكتابة ما تريد ترجمته!")

    trans = await gtrans(text, lan)
    if not trans:
        return await edit_delete(event, "**تحقق من رمز اللغة !, لا يوجد هكذا لغة**")

    output_str = f"**تمت الترجمة إلى {lan}**\n`{trans}`"
    await edit_or_reply(event, output_str)

@l313l.ar_cmd(pattern="(الترجمة الفورية|الترجمه الفوريه|ايقاف الترجمة|ايقاف الترجمه)")
async def reda(event):
    if gvarstatus("transnow"):
        delgvar("transnow")
        await edit_delete(event, "**᯽︙ تم تعطيل الترجمه الفورية **")
    else:
        addgvar("transnow", "Reda") 
        await edit_delete(event, "**᯽︙ تم تفعيل الترجمه الفورية**")

@l313l.ar_cmd(pattern="لغة الترجمة")
async def Reda_is_Here(event):
    t = event.text.replace(".لغة الترجمة", "").strip()
    lang = langs.get(t)
    
    if not lang:
        return await edit_delete(event, "**᯽︙ !تأكد من قائمة اللغات. لا يوجد هكذا لغة**")
    
    addgvar("translang", lang)
    await edit_delete(event, f"**᯽︙ تم تغيير لغة الترجمة إلى {lang} بنجاح ✓ **")

@l313l.on(events.NewMessage(outgoing=True))
async def reda(event):
    if gvarstatus("transnow"):
        if event.media or isinstance(event.media, types.MessageMediaDocument) or isinstance(event.media, types.MessageMediaInvoice):
            return  # لا تترجم إذا كانت رسالة تحتوي على وسائط
        else:
            original_message = event.message.message
            translated_message = await gtrans(soft_deEmojify(original_message.strip()), gvarstatus("translang") or "ar")
            await event.message.edit(translated_message)

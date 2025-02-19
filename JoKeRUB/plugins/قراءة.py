import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from JoKeRUB import l313l

from ..core.managers import edit_delete, edit_or_reply
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البحث"

@l313l.ar_cmd(
    pattern="اقرء(?:\s|$)([\s\S]*)",  # تغيير الحرف من حفظ إلى .اقرء
    command=("اقرء", plugin_category),
    info={
        "header": "لقراءة النص من الصورة",  # تغيير العنوان
        "الاستـخـدام": "{tr}اقرء بالـرد ع صوره",
    },
)
async def _(event):
    if event.fwd_from:
        return
    
    # التحقق إذا كانت الرسالة تحتوي على صورة
    reply_message = await event.get_reply_message()

    if not reply_message:
        await edit_or_reply(event, "**```بالـرد على الصورة حمبـي 🧸🎈```**")
        return

    if not reply_message.media:
        await edit_or_reply(event, "**```بالـرد على صورة وليست نصاً حمبـي 🧸🎈```**")
        return

    chat = "@Saveapostbot"
    processing_msg = await edit_or_reply(event, "**╮ ❐ جاري قراءة النص من الصورة ▬▭... 𓅫╰**")

    async with event.client.conversation(chat) as conv:
        try:
            # إرسال الصورة إلى البوت
            await event.client.forward_messages(chat, reply_message)

            # انتظار الرد من البوت
            response = await conv.get_response()

            # التأكد من وجود رد نصي
            if not response.text:
                await processing_msg.edit("**❌ لم أتمكن من قراءة النص من الصورة! حاول مجددًا.**")
            else:
                await processing_msg.delete()
                await event.client.send_message(event.chat_id, response.text)  # إرسال الرد إلى المحادثة الأصلية

        except YouBlockedUserError:
            await processing_msg.edit(
                "**❈╎تحـقق من أنك لم تقم بحظر البوت .. ثم اعـد استخدام الأمر ...🤖♥️**"
            )
            return
        except Exception as e:
            await processing_msg.edit(f"**❌ حدث خطأ: {str(e)}**")
            return

CMD_HELP.update(
    {
        "قراءة النص من الصورة": "**اسم الإضافة:** قراءة النص من الصورة `\
    \n\n**╮•❐ الأمر:** `.اقرء` بالرد على صورة\
    \n**الشـرح:** استخراج النص من الصورة باستخدام البوت."
    }
)

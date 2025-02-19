import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from JoKeRUB import l313l

from ..core.managers import edit_delete, edit_or_reply
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البحث"

@l313l.ar_cmd(
    pattern="اقرء(?:\s|$)([\s\S]*)",
    command=("اقرء", plugin_category),
    info={
        "header": "لقراءة النص من الصورة",
        "الاستـخـدام": "{tr}اقرء",
    },
)
async def _(event):
    if event.fwd_from:
        return

    reply_message = await event.get_reply_message()

    # التحقق من وجود رسالة رد تحتوي على وسائط (صورة أو فيديو أو مستند)
    if not reply_message:
        await edit_or_reply(event, "**يجب الرد على صورة أو وسائط لاستخراج النص منها! 🖼️❌**")
        return

    if not reply_message.media:
        # إذا كانت الرسالة تحتوي على نص فقط
        await edit_or_reply(event, "**يجب الرد على صورة أو وسائط وليس نصًا! 🖼️❌**")
        return

    chat = "@Saveapostbot"
    processing_msg = await edit_or_reply(event, "**╮ ❐ تم قرائه النص بنجاح @Saveapostbot ▬▭... 𓅫╰**")

    async with event.client.conversation(chat) as conv:
        try:
            # إرسال الصورة إلى البوت
            await event.client.forward_messages(chat, reply_message)

            # الانتظار للحصول على الرد من البوت
            response = await conv.get_response()

            # التأكد من وجود نص في الرد
            if not response.text:
                await processing_msg.edit("**❌ لم أتمكن من قراءة النص من الصورة! حاول مجددًا.**")
            else:
                await processing_msg.delete()
                await event.reply(response.text)  # إرسال الرد إلى نفس المحادثة

        except YouBlockedUserError:
            await processing_msg.edit(
                "**❈╎يبدو أنك حظرت البوت! 🚫\nقم بإلغاء الحظر عبر الذهاب إلى محادثته ثم أعد استخدام الأمر... 🤖♥️**"
            )
            return
        except Exception as e:
            await processing_msg.edit(f"**❌ حدث خطأ: {str(e)}**")
            return

CMD_HELP.update(
    {
        "اقرء": "**اسم الإضافة:** اقرء `\
    \n\n**╮•❐ الأمر:** `.اقرء` \
    \n**الشـرح:** استخدم هذا الأمر بالرد على صورة أو وسائط لاستخراج النص الموجود فيها."
    }
)

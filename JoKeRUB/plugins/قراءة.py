import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from JoKeRUB import l313l

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البحث"

@l313l.ar_cmd(
    pattern="اقرء(?:\s|$)([\s\S]*)",
    command=("اقرء", plugin_category),
    info={
        "header": "لـ استخلاص النصوص من الصور",
        "الاستـخـدام": "{tr}اقرء بالرد على صورة",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message or not reply_message.media:
        await edit_or_reply(event, "**❌ يرجى الرد على صورة لاستخراج النص منها.**")
        return

    chat = "@Saveapostbot"
    processing_message = await edit_or_reply(event, "** تم التحميل بنجاح @Saveapostbot **")

    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=6247895275)  # تحقق من ID البوت الصحيح
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await processing_message.edit(
                "**❌ تأكد من أنك لم تقم بحظر البوت @ZIKOD12bot ثم أعد المحاولة.**"
            )
            return

        if response.text.startswith("❌"):
            await processing_message.edit("**🚫 لم يتمكن البوت من استخراج النص من الصورة.**")
        else:
            await processing_message.delete()
            await event.client.send_message(event.chat_id, response.message)

CMD_HELP.update(
    {
        "اقرء": "**اسم الإضافة:** `اقرء`\
    \n\n**🔹 الأمر:** `.اقرء` بالرد على صورة\
    \n**🔹 الوصف:** استخراج النصوص من الصور باستخدام بوت خارجي."
    }
)


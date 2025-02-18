

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
    pattern="حفظ(?:\s|$)([\s\S]*)",
    command=("حفظ", plugin_category),
    info={
        "header": "لتحميل منشور مقييد ",
        "الاستـخـدام": "{tr}حفظ بالـرد ع رابـط",
    },
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**```بالـرد على الرابـط حمبـي 🧸🎈```**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**```بالـرد على الرابـط حمبـي 🧸🎈```**")
        return
    chat = "@ZIKOD12bot"
    zzzzl1l = await edit_or_reply(event, "**╮ ❐ تم تحميل ملفك بنجاح اهنا حبيبي ب بوت : @ZIKOD12bot  ▬▭... 𓅫╰**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=6748718626)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzzzl1l.edit(
                "**❈╎تحـقق من انـك لم تقـم بحظـر البوت  .. ثم اعـد استخدام الامـر ...🤖♥️**"
            )
            return
        if response.text.startswith(""):
            await zzzzl1l.edit("**🤨💔...؟**")
        else:
            await zzzzl1l.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "محتوا مقييد": "**اسم الاضافـه : **محتوا مقييد`\
    \n\n**╮•❐ الامـر ⦂ **`.حفظ` بالرد على الرابط\
    \n**الشـرح •• **تحميل المنشورات المقيدة "
    }
)

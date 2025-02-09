#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
# Port to ZThon
# modified by @ZedThon
# Copyright (C) 2022.

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
    pattern="تيكتوك(?:\s|$)([\s\S]*)",
    command=("تيكتوك", plugin_category),
    info={
        "header": "لـ تحميل الفيـديـو من تيـك تـوك عبـر الرابـط",
        "الاستـخـدام": "{tr}تيكتوك بالـرد ع رابـط",
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
    chat = "@Bshahjahavvavbot"
    zzzzl1l = await edit_or_reply(event, "**╮ ❐ جـارِ التحميـل من تيـك تـوك انتظر 2ثانيه وخذ الفديومن البوت: @Bshahjahavvavbot ▬▭... 𓅫╰**")
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
                "**❈╎تحـقق من انـك لم تقـم بحظـر البوت @Bshahjahavvavbot .. ثم اعـد استخدام الامـر ...🤖♥️**"
            )
            return
        if response.text.startswith(""):
            await zzzzl1l.edit("**🤨💔...؟**")
        else:
            await zzzzl1l.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "تيك توك": "**اسم الاضافـه : **`تيك توك`\
    \n\n**╮•❐ الامـر ⦂ **`.تيكتوك` بالرد على الرابط\
    \n**الشـرح •• **تحميل مقاطـع الفيديـو من تيـك تـوك"
    }
)

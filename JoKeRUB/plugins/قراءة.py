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
    pattern="قرائه(?:\s|$)([\s\S]*)",
    command=("قرائه", plugin_category),
    info={
        "header": "لقرائة النص من الصورة",
        "الاستـخـدام": "{tr}قرائه",
    },
)
async def _(event):
    if event.fwd_from:
        return

    reply_message = await event.get_reply_message()
    
    if not reply_message:
        await edit_or_reply(event, "**بالـرد على صورة لاستخراج النص 🖼️**")
        return

    if not reply_message.media:
        await edit_or_reply(event, "**يجب الرد على صورة وليس على نص 🖼️❌**")
        return

    chat = "@Saveapostbot"
    zzzzl1l = await edit_or_reply(event, "**╮ ❐ جـارِ القراءة ▬▭... 𓅫╰**")

    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=chat))
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzzzl1l.edit(
                "**❈╎قم بإلغاء حظر البوت عبر الذهاب إلى محادثته، ثم أعد استخدام الأمر... 🤖♥️**"
            )
            return

        if not response.text:
            await zzzzl1l.edit("**🤨💔 لم أتمكن من قراءة النص من الصورة...**")
        else:
            await zzzzl1l.delete()
            await event.client.send_message(event.chat_id, response.message)

CMD_HELP.update(
    {
        "قرائه": "**اسم الإضافة :** قرائه `\
    \n\n**╮•❐ الأمر ⦂** `.قرائه` \
    \n**الشـرح •• ** استخدم هذا الأمر بالرد على صورة لاستخراج النص الموجود فيها"
    }
)



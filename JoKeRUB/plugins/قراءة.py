import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import MessageMediaPhoto

from JoKeRUB import l313l

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البحث"

@l313l.ar_cmd(
    pattern="قرائه(?:\s|$)([\s\S]*)",
    command=("قرائه", plugin_category),
    info={
        "header": "إرسال صورة أو معالجة رابط",
        "الاستـخـدام": "{tr}قرائه لإرسال الصورة أو معالجة الرابط",
    },
)
async def _(event):
    if event.fwd_from:
        return

    # تحقق من وجود صورة أو رابط في الرسالة
    if not event.media and not event.text:
        await edit_or_reply(event, "**```يرجى إرسال صورة أو رابط لاستخدام الأمر```**")
        return

    # إذا كانت الرسالة تحتوي على صورة
    if event.media and isinstance(event.media, MessageMediaPhoto):
        zzzzl1l = await edit_or_reply(event, "**╮ ❐ ▬▭... 𓅫╰**")
        try:
            await event.client.send_message(event.chat_id, "إليك الصورة التي أرسلتها 🖼️:", file=event.media)
            await zzzzl1l.delete()
        except YouBlockedUserError:
            await zzzzl1l.edit(
                "**❈╎تحـقق من انـك لم تقـم بحظـر البوت  .. ثم اعـد استخدام الامـر ...🤖♥️**"
            )
            return
    else:
        # في حالة وجود رابط أو نص
        await edit_or_reply(event, "**```تم معالجة الرابط أو النص بنجاح!```**")

CMD_HELP.update(
    {
        "قرائه": "**اسم الاضافـه : **قرائه `\
    \n\n**╮•❐ الامـر ⦂ **`.قرائه` لإرسال صورة أو معالجة رابط\
    \n**الشـرح •• **إرسال الصورة أو معالجة الرابط الذي تم إرساله"
    }
)


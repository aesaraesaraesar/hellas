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

    # التحقق من وجود رسالة رد
    if not reply_message:
        await edit_or_reply(event, "**❌ يجب الرد على صورة أو وسائط لاستخراج النص منها! 🖼️**")
        return

    # التحقق من وجود وسائط (media) في الرسالة
    if not reply_message.media:
        await edit_or_reply(event, "**❌ الرسالة التي رددت عليها لا تحتوي على صورة أو وسائط! 🖼️**")
        return

    chat = "@Saveapostbot"
    processing_msg = await edit_or_reply(event, "**🔄 جارٍ قراءة النص من الصورة... 📖**")

    async with event.client.conversation(chat) as conv:
        try:
            # إرسال الصورة إلى البوت
            await event.client.forward_messages(chat, reply_message)

            # انتظار الرد من البوت
            response = await conv.get_response()

            # التأكد من أن الرد يحتوي على نص
            if not response.text:
                await processing_msg.edit("**❌ لم أتمكن من استخراج النص من الصورة! حاول مجددًا.**")
                return

            # حذف رسالة "جارٍ القراءة" وإرسال النص المستخرج إلى نفس المحادثة
            await processing_msg.delete()
            await event.reply(response.text)  # استخدام event.reply لإرسال الرد في نفس المحادثة

        except YouBlockedUserError:
            await processing_msg.edit(
                "**🚫 يبدو أنك حظرت البوت @Saveapostbot!\nقم بإلغاء الحظر ثم أعد استخدام الأمر. 🤖**"
            )
            return
        except Exception as e:
            await processing_msg.edit(f"**❌ حدث خطأ أثناء استخراج النص: {str(e)}**")
            return

CMD_HELP.update(
    {
        "اقرء": "**📌 اسم الإضافة:** `اقرء` \
    \n\n**📝 الأمر:** `.اقرء` \
    \n**🔍 الوصف:** استخدم هذا الأمر بالرد على صورة لاستخراج النص الموجود فيها وإرساله في نفس المحادثة."
    }
)






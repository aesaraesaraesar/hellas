from JoKeRUB import l313l
from ..core.managers import edit_or_reply

plugin_category = "البحث"

@l313l.ar_cmd(
    pattern="(السورس|سورس)$",
    command=("السورس", plugin_category),
    info={
        "header": "لعرض شرح استخدام سورس هيلاس",
        "الاستـخـدام": "{tr}السورس أو {tr}سورس",
    },
)
async def _(event):
    await edit_or_reply(
        event,
        "✳️ **سورس هيلاس - HELLAS USERBOT** ✳️\n\n"
        "📽️ **الشرح الكامل للسورس:**\n"
        "↪️ [اضغط هنا للمشاهدة](https://youtu.be/h0IIIkfxw30?si=9VKXcKhbBRFKlwoW)\n\n"
        "📢 **قناة السورس:**\n"
        "🔗 [@HELLASUserBot](https://t.me/HELLASUserBot)\n\n"
        "💬 **كروب الدعم والمساعدة:**\n"
        "🔗 [@helashelb](https://t.me/helashelb)\n\n"
        "🛡️ **سورس حماية المجموعات:**\n"
        "🔗 [@SEFHELLAS](https://t.me/SEFHELLAS)\n\n"
        "👨‍💻 **المطور المسؤول:**\n"
        "🔗 [@F_Q_1](https://t.me/F_Q_1)"
    )

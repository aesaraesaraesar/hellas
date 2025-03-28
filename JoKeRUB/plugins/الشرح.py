from JoKeRUB import l313l
from ..core.managers import edit_or_reply

plugin_category = "البحث"

@l313l.ar_cmd(
    pattern="الشرح$",
    command=("الشرح", plugin_category),
    info={
        "header": "لعرض شرح استخدام سورس هيلاس",
        "الاستـخـدام": "{tr}الشرح",
    },
)
async def _(event):
    await edit_or_reply(
        event, 
        "📌 **شرح استخدام سورس هيلاس:**\n\n🔗 [اضغط هنا للمشاهدة](https://youtu.be/h0IIIkfxw30?si=9VKXcKhbBRFKlwoW)"
    )


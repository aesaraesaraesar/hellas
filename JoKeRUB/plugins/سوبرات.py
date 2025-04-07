from JoKeRUB import l313l
from ..core.managers import edit_or_reply

plugin_category = "البحث"

@l313l.ar_cmd(
    pattern="(سوبريه|سوبرات|روابط سوبريه|روابط سوبرات|السوبرات)$",
    command=("سوبريه", plugin_category),
    info={
        "header": "لعرض رابط سوبرات",
        "الاستـخـدام": "{tr}سوبريه أو {tr}سوبرات أو {tr}روابط سوبريه أو {tr}روابط سوبرات أو {tr}السوبرات",
    },
)
async def _(event):
    await edit_or_reply(
        event,
        "🔗 [اضغط هنا للانتقال إلى سوبرات](https://t.me/BEEBB)"
    )


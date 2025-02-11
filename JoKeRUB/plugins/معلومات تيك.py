from JoKeRUB import l313l
import aiohttp
from telethon import events

@client.on(events.NewMessage(pattern=r"^\.رابط\s+(https?://\S+)"))
async def ssWeb(event):
    msg = event.message
    await event.reply("**⏳ جاري التقاط لقطة الشاشة...**")
    
    if msg.text:
        lnk = msg.text.split()[1]
        params = {
            "tkn": "125",
            "d": "3000",
            "u": lnk,
            "fs": "0",
            "w": "1280",
            "h": "1200",
            "s": "100",
            "z": "100",
            "f": "jpg",
            "rt": "jweb",
        }

        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.pikwy.com/", params=params) as res:
                try:
                    data = await res.json()
                    img = data["iurl"]
                    date = data["date"]
                    await event.reply(f"**✅ تم التقاط لقطة الشاشة بنجاح!**", file=img)
                except KeyError:
                    await event.respond(f"❌ **فشل التقاط لقطة الشاشة، تأكد من الرابط!**")


from telethon import events, Button
from ..Config import Config
from l313l.razan.resources.mybot import *

if Config.TG_BOT_USERNAME and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        query = event.text.lower()  

        if query.startswith("السورس") and event.query.user_id == bot.uid:
            buttons = [
                [Button.url("1- قناه السورس", "https://t.me/HELLASUserBot"), 
                 Button.url("2- استخراج ايبيات", "https://my.telegram.org/")],
                [Button.url("3- استخراج تيرمكس", "https://t.me/bothellasbot"), 
                 Button.url("4- بوت فاذر", "http://t.me/BotFather")],
                [Button.url("5- اسعار التنصيب", "https://t.me/HELLASUserBot/66")],
                [Button.url("المطـور 👨🏼‍💻", "https://t.me/F_Q_1")]
            ]

            result = builder.article(title=" ", text=" ", buttons=buttons, link_preview=False)  
            await event.answer([result])

@bot.on(events.NewMessage(pattern="السورس"))  
async def repo(event):
    TG_BOT = Config.TG_BOT_USERNAME
    response = await bot.inline_query(TG_BOT, "السورس")
    
    if response:
        await response[0].click(event.chat_id)
    
    await event.delete()


from JoKeRUB import l313l
from telethon import events

client = l313l  # نفترض أن l313l هو كائن جاهز لجلسة Telethon

# متغير لتتبع حالة الرد التلقائي
auto_reply_enabled = True  

@client.on(events.NewMessage)
async def handler(event):
    global auto_reply_enabled  # السماح بتعديل الحالة داخل الدالة
    sender = await event.get_sender()
    
    if sender.bot:
        return  # تجاهل الرسائل الواردة من البوتات

    # تفعيل الرد التلقائي عند إرسال ".تفعيل الرد التلقائي."
    if event.raw_text.strip() == ".تفعيل الرد التلقائي.":
        auto_reply_enabled = True
        await event.reply("✅ تم تفعيل الرد التلقائي!")
        return
    
    # تعطيل الرد التلقائي عند إرسال ".إيقاف الرد التلقائي."
    if event.raw_text.strip() == ".إيقاف الرد التلقائي.":
        auto_reply_enabled = False
        await event.reply("⛔ تم تعطيل الرد التلقائي!")
        return

    # الرد التلقائي فقط إذا كان مفعلاً
    if auto_reply_enabled:
        await event.reply("أنا موجود، جئت لأرد عليك!")

async def main():
    print("✅ تم تشغيل البوت...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())

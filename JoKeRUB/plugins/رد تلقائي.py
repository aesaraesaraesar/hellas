from JoKeRUB import l313l
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest

client = l313l  # نفترض أن l313l هو كائن جاهز لجلسة Telethon

# متغيرات التحكم
auto_reply_enabled = False  # الرد التلقائي مبدئيًا غير مفعل
custom_reply_message = "أنا غير متصل حاليًا، سأرد عليك لاحقًا!"  # الكليشة الافتراضية

@client.on(events.NewMessage)
async def handler(event):
    global auto_reply_enabled, custom_reply_message
    sender = await event.get_sender()

    # تجاهل الرسائل من البوتات أو إذا لم تكن المحادثة خاصة
    if sender.bot or not event.is_private:
        return  

    # تجاهل الرسائل التي أرسلها الشخص نفسه (مالك الجلسة)
    if sender.id == (await client.get_me()).id:
        return  # تجاهل رسائلك الخاصة

    # تفعيل الرد التلقائي
    if event.raw_text.strip() == ".تفعيل الرد التلقائي.":
        auto_reply_enabled = True
        await event.reply("✅ تم تفعيل الرد التلقائي في الخاص!")
        return
    
    # تعطيل الرد التلقائي
    if event.raw_text.strip() == ".إيقاف الرد التلقائي.":
        auto_reply_enabled = False
        await event.reply("⛔ تم تعطيل الرد التلقائي في الخاص!")
        return

    # تعيين كليشة الرد التلقائي
    if event.raw_text.startswith(".تعيين الكليشة "):
        custom_reply_message = event.raw_text.replace(".تعيين الكليشة ", "").strip()
        await event.reply(f"✅ تم تعيين الكليشة الجديدة:\n\n**{custom_reply_message}**")
        return

    # الحصول على حالة المستخدم (Online / Offline)
    user_status = (await client(GetFullUserRequest("me"))).full_user

    # التحقق إذا كنت متصل (لن يرد إذا كنت أونلاين)
    if hasattr(user_status, "status") and user_status.status is not None:
        if user_status.status.__class__.__name__ == "UserStatusOnline":
            return  # إذا كنت أونلاين، لا يرسل أي رد

    # الرد التلقائي فقط إذا كنت غير متصل وتم تفعيل الرد
    if auto_reply_enabled:
        await event.reply(custom_reply_message)

async def main():
    print("✅ تم تشغيل البوت، ويعمل فقط في المحادثات الخاصة...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())

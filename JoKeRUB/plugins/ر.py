from JoKeRUB import l313l
import asyncio

auto_reply_enabled = False  # متغير لتفعيل وتعطيل الرد التلقائي

@l313l.on(events.NewMessage(pattern=".تفعيل الرد التلقائي"))
async def enable_auto_reply(event):
    global auto_reply_enabled
    auto_reply_enabled = True
    await event.reply("✅ تم تفعيل الرد التلقائي في التعليقات.")

@l313l.on(events.NewMessage(pattern=".تعطيل الرد التلقائي"))
async def disable_auto_reply(event):
    global auto_reply_enabled
    auto_reply_enabled = False
    await event.reply("❌ تم تعطيل الرد التلقائي في التعليقات.")

@l313l.on(events.NewMessage(incoming=True))  # يعمل على أي قناة
async def auto_reply(event):
    global auto_reply_enabled
    if auto_reply_enabled:
        words = event.text.split()
        if len(words) > 1:
            reply_text = " ".join(words[1:])
            await l313l.send_message(event.chat_id, reply_text, comment_to=event.id)

print("✅ البوت يعمل بنجاح!")
l313l.run_until_disconnected()

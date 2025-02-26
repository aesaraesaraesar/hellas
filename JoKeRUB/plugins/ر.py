from JoKeRUB import l313l
from telethon import events  # استيراد events
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

@l313l.on(events.NewMessage(chats=lambda e: e.is_channel and e.is_reply))  # يعمل فقط على تعليقات القنوات
async def auto_reply(event):
    global auto_reply_enabled
    if auto_reply_enabled:
        words = event.text.split()
        if len(words) > 1:
            reply_text = words[-1]  # يأخذ آخر كلمة فقط
            await l313l.send_message(event.chat_id, reply_text, comment_to=event.id)

print("✅ البوت يعمل بنجاح!")
l313l.run_until_disconnected()



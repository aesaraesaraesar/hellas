import asyncio
from telethon import TelegramClient, events
from JoKeRUB import l313l
from ..Config import Config

plugin_category = "البوت"

@l313l.on(events.NewMessage(pattern='.مغادرة'))
async def leave_all_channels(event):
    # تحقق مما إذا كان المرسل هو الحساب المنصب فقط
    if event.sender_id != 7095300880:  # تأكد من استبدال Config.OWNER_ID بمعرف صاحب الحساب
        return

    await event.reply("جاري مغادرة جميع القنوات...")

    try:
        async for dialog in l313l.iter_dialogs():
            if dialog.is_channel:
                await dialog.click()  # الانضمام للقناة (إذا لزم الأمر)
                await l313l.leave_dialog(dialog)  # مغادرة القناة
                await event.reply(f"✅ مغادرة القناة: {dialog.title}")

        await event.reply("✅ تم مغادرة جميع القنوات بنجاح.")
    except Exception as e:
        await event.reply(f"خطأ ❌: {e}")

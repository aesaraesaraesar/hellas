import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.channels import LeaveChannelRequest
from JoKeRUB import l313l
from ..Config import Config

plugin_category = "البوت"

@l313l.on(events.NewMessage(pattern='.مغادرة'))
async def leave_all_channels(event):
    # تحقق مما إذا كان المرسل هو الحساب المنصب فقط
    if event.sender_id != Config.OWNER_ID:
        return

    await event.reply("جاري مغادرة جميع القنوات...")

    try:
        async for dialog in l313l.iter_dialogs():
            if dialog.is_channel:
                await l313l(LeaveChannelRequest(dialog.entity))  # مغادرة القناة
                await event.reply(f"✅ مغادرة القناة: {dialog.title}")

        await event.reply("✅ تم مغادرة جميع القنوات بنجاح.")
    except Exception as e:
        await event.reply(f"❌ حدث خطأ: {str(e)}")

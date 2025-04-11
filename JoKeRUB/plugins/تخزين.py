from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.messages import CreateChatRequest
from telethon.tl.types import PeerUser
import config

# استخدام الجلسة النصية
client = TelegramClient(StringSession(config.STRING_SESSION), config.api_id, config.api_hash)

async def get_or_create_storage_group():
    dialogs = await client.get_dialogs()
    storage_group = None
    for dialog in dialogs:
        if dialog.name == "مجموعة التخزين":
            storage_group = dialog.entity
            break

    if not storage_group:
        storage_group = await client(CreateChatRequest(
            users=[], title="مجموعة التخزين"
        ))
        storage_group = storage_group.chats[0]
    return storage_group

@client.on(events.NewMessage(incoming=True))
async def forward_to_storage_group(event):
    if isinstance(event.peer_id, PeerUser):
        sender = await event.get_sender()
        if not sender.bot:
            storage_group = await get_or_create_storage_group()
            await client.forward_messages(storage_group.id, event.message)

async def main():
    print("تم تسجيل الدخول بنجاح.")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())

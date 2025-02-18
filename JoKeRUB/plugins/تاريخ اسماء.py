from telethon import TelegramClient, events
from JoKeRUB import l313l
from config import API_ID, API_HASH

client = TelegramClient('session_name', API_ID, API_HASH)

@client.on(events.NewMessage(pattern=r'\.تاريخ (.+)'))
async def search_old_names(event):
    username = event.pattern_match.group(1)
    try:
        user = await client.get_entity(username)
        history = await client(GetUserFullRequest(user.id))
        old_names = history.user.first_name  # تعديل لاسترجاع الأسماء القديمة
        await event.reply(f'الأسماء القديمة لليوزر @{username}:
{old_names}')
    except Exception as e:
        await event.reply(f'حدث خطأ: {str(e)}')

print("Client is running...")
client.start()
client.run_until_disconnected()


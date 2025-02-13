from JoKeRUB import *
from JoKeRUB import l313l
from JoKeRUB.utils import admin_cmd
from telethon.tl.types import Channel, Chat, User
from telethon.tl import functions, types
from telethon.tl.functions.messages import  CheckChatInviteRequest, GetFullChatRequest
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
#Jepthon old

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    
    try:
        return await event.client(functions.channels.GetFullChannelRequest(chat))
    except Exception:
        await event.reply("⚠️ لا يمكن العثور على المجموعة أو القناة.")
        return None

# 🟢 وظيفة إضافة أعضاء من مجموعة أخرى
@l313l.on(admin_cmd(pattern=r"ضيف ?(.*)"))
async def add_users(event):   
    sender = await event.get_sender()
    me = await event.client.get_me()

    if sender.id != me.id:
        msg = await event.reply("🔄 جاري تنفيذ العملية... الرجاء الانتظار.")
    else:
        msg = await event.edit("🔄 جاري تنفيذ العملية... الرجاء الانتظار.")

    target_chat_info = await get_chatinfo(event)
    if not target_chat_info:
        return
    
    target_chat_id = target_chat_info.full_chat.id
    current_chat = await event.get_chat()

    if event.is_private:
        return await msg.edit("⚠️ لا يمكن إضافة المستخدمين هنا.")
    
    success = 0
    failed = 0
    last_error = "لا يوجد أخطاء"

    await msg.edit("📥 جاري جمع معلومات المستخدمين...")

    async for user in event.client.iter_participants(target_chat_id):
        try:
            await event.client(functions.channels.InviteToChannelRequest(channel=current_chat, users=[user.id]))
            success += 1
            await asyncio.sleep(2)  # تأخير لمنع الحظر
        except (UserPrivacyRestrictedError, UserNotMutualContactError):
            failed += 1
            last_error = "🔒 خصوصية المستخدم تمنع إضافته"
        except UserChannelsTooMuchError:
            failed += 1
            last_error = "📛 المستخدم في عدد كبير جدًا من القنوات"
        except UserKickedError:
            failed += 1
            last_error = "🚫 المستخدم محظور في المجموعة"
        except ChatAdminRequiredError:
            return await msg.edit("⚠️ يجب أن أكون مشرفًا لإضافة أعضاء.")
        except PeerFloodError:
            return await msg.edit("⚠️ تم حظري مؤقتًا بسبب كثرة الدعوات! حاول لاحقًا.")
        except FloodWaitError as e:
            return await msg.edit(f"⏳ تيليجرام فرض انتظار {e.seconds} ثانية! حاول لاحقًا.")
        except Exception as e:
            failed += 1
            last_error = str(e)
        
        await msg.edit(f"✅ تمت إضافة: {success}\n❌ فشل الإضافة: {failed}\n🛠 آخر خطأ: {last_error}")

    await msg.edit(f"🎉 تمت العملية بنجاح!\n✅ أضيف: {success}\n❌ لم يتم إضافة: {failed}")

# 🟢 وظيفة إضافة جميع جهات الاتصال للمجموعة
@l313l.on(admin_cmd(pattern=r"اضافة_جهاتي ?(.*)"))
async def add_contacts(event):
    current_chat = event.chat_id

    if event.is_private:
        return await event.reply("⚠️ لا يمكنني إضافة جهات الاتصال هنا.")

    contacts = await event.client(functions.contacts.GetContactsRequest(hash=0))
    success = 0
    failed = 0
    last_error = "لا يوجد أخطاء"

    msg = await event.reply("📤 جاري إضافة جهات الاتصال...")

    for user in contacts.users:
        try:
            await event.client(functions.channels.InviteToChannelRequest(channel=current_chat, users=[user.id]))
            success += 1
            await asyncio.sleep(2)  # تأخير لمنع الحظر
        except (UserPrivacyRestrictedError, UserNotMutualContactError):
            failed += 1
            last_error = "🔒 خصوصية المستخدم تمنع إضافته"
        except UserChannelsTooMuchError:
            failed += 1
            last_error = "📛 المستخدم في عدد كبير جدًا من القنوات"
        except UserKickedError:
            failed += 1
            last_error = "🚫 المستخدم محظور في المجموعة"
        except ChatAdminRequiredError:
            return await msg.edit("⚠️ يجب أن أكون مشرفًا لإضافة الأعضاء.")
        except PeerFloodError:
            return await msg.edit("⚠️ تم حظري مؤقتًا بسبب كثرة الدعوات! حاول لاحقًا.")
        except FloodWaitError as e:
            return await msg.edit(f"⏳ تيليجرام فرض انتظار {e.seconds} ثانية! حاول لاحقًا.")
        except Exception as e:
            failed += 1
            last_error = str(e)

        await msg.edit(f"✅ تمت إضافة: {success}\n❌ فشل الإضافة: {failed}\n🛠 آخر خطأ: {last_error}")

    await msg.edit(f"🎉 تمت العملية بنجاح!\n✅ أضيف: {success}\n❌ لم يتم إضافة: {failed}")

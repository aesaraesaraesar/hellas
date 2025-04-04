#    جميع الحقوق لمطوري سورس روبن حصريا لهم فقط
#    اذا تخمط الملف اذك الحقوق وكاتبيه ومطوريه لا تحذف الحقوق وتصير فاشل 👍
#    كتابة الشسد 
import asyncio
import io
import re

from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest
from JoKeRUB import bot
from JoKeRUB.sql_helper.blacklist_assistant import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from JoKeRUB.sql_helper.botusers_sql import add_me_in_db, his_userid
from JoKeRUB.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)
from l313l.razan.resources.assistant import *

import asyncio
import io
import re
import uuid
import os
from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest, GetFullChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

user_sessions = {}
collecting = {}
account_numbers = []

api_id = '21166913'
api_hash = '70fc0a6dd6f4133a2477902e27133af6'

def save_sessions_to_file():
    file_name = f"sessions_{uuid.uuid4().hex}.txt"
    with open(file_name, 'w') as f:
        for session in user_sessions.values():
            if 'session_code' in session:
                f.write(session['session_code'] + '\n')
    return file_name

@tgbot.on(events.NewMessage(pattern="^/he"))
async def handle_con_command(event):
    username = event.sender.username if event.sender.username else "مستخدم"
    bot_info = (
        "🔹معلومات البوت:\n"
        "بوت التجميع الخاص بنا يساعدك في تجميع النقاط والخدمات المختلفة من تليجرام.\n"
        "استخدم الأزرار التالية للتفاعل مع البوت:"
    )
    buttons = [
        [Button.inline('تسجيل الدخول 🔑', b'login'), Button.inline('تسجيل جلسة 📝', b'add_session')],
        [Button.inline('قسم النقاط 📊', b'point_section')],
        [Button.inline('هدية خدمات تليجرام 🎁', b'open_bot')],
        [Button.inline('حذف حساب 🗑️', b'delete_account'), Button.inline('عدد الحسابات 📊', b'account_count')],
        [Button.inline('حذف جلسة ❌', b'delete_session'), Button.inline('إيقاف التجميع ⛔', b'stop_collecting')],
        [Button.inline('سحب تخزين 📂', b'get_storage'), Button.inline('تسجيل تخزين 📥', b'upload_storage')],
        [Button.inline('تقليد', b'mimic')]
    ]
    
    await event.reply(f"المالك @{username}\n\n{bot_info}", buttons=buttons)

@tgbot.on(events.CallbackQuery(data=b'mimic'))
async def handle_mimic_button(event):
    await event.edit("سوف أقوم بتقليدك الآن، ارسل أي رسالة.")
    tgbot.add_event_handler(mimic_user, events.NewMessage(from_users=event.sender_id))

async def mimic_user(event):
    await event.reply(event.text)

@tgbot.on(events.CallbackQuery(data=b'point_section'))
async def point_section(event):
    buttons = [
        [Button.inline('نقاط المليار 📈', b'points_milyar')],
        [Button.inline('نقاط ارشقلي🏆', b'points_milyon')],
        [Button.inline('نقاط مهدوينو🔥', b'points_3qab')],
        [Button.inline('العودة للخلف 🔙', b'back_to_main')]
    ]
    await event.reply("اختر أحد الخيارات التالية:", buttons=buttons)

@tgbot.on(events.CallbackQuery(data=b'points_milyar'))
async def points_milyar(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("📈 **سيتم تجميع النقاط من بوت المليار**")
        bot_username = '@EEObot'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@tgbot.on(events.CallbackQuery(data=b'points_milyon'))
async def points_milyon(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("🏆 **سيتم تجميع النقاط من بوت المليون**")
        bot_username = '@qweqwe1919bot'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@tgbot.on(events.CallbackQuery(data=b'points_3qab'))
async def points_3qab(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("🔥 **سيتم تجميع النقاط من بوت العقاب**")
        bot_username = '@MARKTEBOT'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@tgbot.on(events.CallbackQuery(data=b'back_to_main'))
async def back_to_main(event):
    await handle_con_command(event)

@tgbot.on(events.CallbackQuery(data=b'login'))
async def login(event):
    await event.respond("الرجاء إرسال رقم الهاتف مع كود الدولة:")
    user_sessions[event.sender_id] = {"step": "phone"}

@tgbot.on(events.CallbackQuery(data=b'add_session'))
async def add_session(event):
    await event.respond("الرجاء إرسال كود الجلسة (StringSession):")
    user_sessions[event.sender_id] = {"step": "session_code"}

@tgbot.on(events.CallbackQuery(data=b'delete_session'))
async def delete_session(event):
    await event.respond("الرجاء إرسال كود الجلسة (StringSession) التي ترغب في حذفها:")
    user_sessions[event.sender_id] = {"step": "delete_session_code"}

@tgbot.on(events.CallbackQuery(data=b'stop_collecting'))
async def stop_collecting(event):
    collecting[event.sender_id] = False
    await event.reply("تم إيقاف التجميع ⛔")

@tgbot.on(events.CallbackQuery(data=b'get_storage'))
async def get_storage(event):
    file_name = save_sessions_to_file()
    await event.reply("تم حفظ الجلسات. إليك الملف:", file=file_name)

@tgbot.on(events.CallbackQuery(data=b'upload_storage'))
async def upload_storage(event):
    await event.respond("الرجاء إرسال ملف التخزين:")
    user_sessions[event.sender_id] = {"step": "upload_storage"}

@tgbot.on(events.NewMessage)
async def handle_new_message(event):
    if event.sender_id in user_sessions:
        step = user_sessions[event.sender_id]["step"]
        if step == "phone":
            phone = event.message.message
            client = TelegramClient(StringSession(), api_id, api_hash, app_version="Robin")
            user_sessions[event.sender_id].update({"client": client, "phone": phone})
            await client.connect()
            await client.send_code_request(phone)
            await event.reply("الرجاء إرسال كود الدخول بشكل مسافات (مثال: 1 2 3 4 5):")
            user_sessions[event.sender_id]["step"] = "code"
        elif step == "code":
            code = event.message.message.replace(" ", "")
            client = user_sessions[event.sender_id]["client"]
            phone = user_sessions[event.sender_id]["phone"]
            try:
                await client.sign_in(phone, code)
                await event.reply(
                    "تم تسجيل الدخول بنجاح!",
                    buttons=[Button.inline('تسجيل رقم آخر 🔄', b'login')]
                )
                user_sessions[event.sender_id]["step"] = None
            except Exception as e:
                if 'password' in str(e).lower():
                    await event.reply("الرجاء إرسال كلمة السر:")
                    user_sessions[event.sender_id]["step"] = "password"
                else:
                    await event.reply(f"حدث خطأ: {str(e)}")
                    del user_sessions[event.sender_id]
        elif step == "password":
            password = event.message.message
            client = user_sessions[event.sender_id]["client"]
            try:
                if password.lower() != 'لا':
                    await client.sign_in(password=password)
                await event.reply(
                    "تم تسجيل الدخول بنجاح!",
                    buttons=[Button.inline('تسجيل رقم آخر 🔄', b'login')]
                )
                session_str = client.session.save()  # حفظ جلسة المستخدم
                user_sessions[event.sender_id]["session_name"] = session_str
                account_numbers.append(user_sessions[event.sender_id]["phone"])
                user_sessions[event.sender_id]["step"] = None
            except Exception as e:
                await event.reply(f"حدث خطأ: {str(e)}")
                del user_sessions[event.sender_id]
        elif step == "session_code":
            session_code = event.message.message
            try:
                client = TelegramClient(StringSession(session_code), api_id, api_hash)
                await client.connect()
                await event.reply(
                    "تم تسجيل الجلسة بنجاح!",
                    buttons=[Button.inline('تسجيل جلسة أخرى 🔄', b'add_session')]
                )
                user_sessions[event.sender_id]["client"] = client
                user_sessions[event.sender_id]["session_code"] = session_code
                user_sessions[event.sender_id]["step"] = None
                save_sessions_to_file()  # حفظ الجلسات في الملف
            except Exception as e:
                await event.reply(f"حدث خطأ: {str(e)}")
                del user_sessions[event.sender_id]
        elif step == "delete_session_code":
            session_code = event.message.message
            found = False
            for user_id, session in user_sessions.items():
                if session.get("session_code") == session_code:
                    del user_sessions[user_id]
                    found = True
                    break
            if found:
                await event.reply("تم حذف الجلسة بنجاح!")
            else:
                await event.reply("لم يتم العثور على الجلسة.")
            del user_sessions[event.sender_id]
        elif step == "upload_storage":
            if event.file:
                file_path = await event.download_media()
                with open(file_path, 'r') as f:
                    sessions = f.readlines()
                count = 0
                for session_code in sessions:
                    session_code = session_code.strip()
                    if session_code and session_code not in user_sessions:
                        client = TelegramClient(StringSession(session_code), api_id, api_hash)
                        await client.connect()
                        user_sessions[session_code] = {"client": client, "session_code": session_code}
                        count += 1
                await event.reply(f"تم إضافة {count} رقم إلى البوت")
                os.remove(file_path)
            del user_sessions[event.sender_id]
    else:
        # التحقق من الرسائل التي تحتوي على روابط قنوات الاشتراك
        links = re.findall(r'https://t\.me/[^\s]+', event.message.message)
        if links:
            client = user_sessions[event.sender_id]["client"]
            for link in links:
                try:
                    if 'joinchat' in link or '+' in link:
                        invite_code = link.split('/')[-1]
                        await client(ImportChatInviteRequest(invite_code))
                    else:
                        await client(JoinChannelRequest(link))
                    await asyncio.sleep(2)
                except Exception as e:
                    await event.reply(f"حدث خطأ أثناء الانضمام إلى القناة: {str(e)}")

@tgbot.on(events.CallbackQuery(data=b'open_bot'))
async def open_bot(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        bot_username9 = '@SMSMEGbot'
        await client.send_message(bot_username9, '/start')
        await asyncio.sleep(4)
        msg = await client.get_messages(bot_username9, limit=1)
        if msg[0].buttons:
            await msg[0].click(text='الإعدادات وجمع النقاط 🔑')
            await asyncio.sleep(4)
            msg = await client.get_messages(bot_username9, limit=1)
            if msg[0].buttons:
                await msg[0].click(text='جمع نقاط ➕')
                await asyncio.sleep(4)
                msg = await client.get_messages(bot_username9, limit=1)
                if msg[0].buttons:
                    await msg[0].click(text='الهدية اليومية 🎁')
                    await event.reply("تم جمع الهدية بنجاح!")
                else:
                    await event.reply("لم يتم العثور على الزر المطلوب في الرسالة الثالثة.")
            else:
                await event.reply("لم يتم العثور على الزر المطلوب في الرسالة الثانية.")
        else:
            await event.reply("لم يتم العثور على الزر المطلوب في الرسالة الأولى.")
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

async def join_channels(bot_username, event, client):
    collecting[event.sender_id] = True
    await client.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await client.get_messages(bot_username, limit=1)
    if msg0[0].buttons and len(msg0[0].buttons) > 2:
        await msg0[0].click(2)
    else:
        await event.reply("لم يتم العثور على الزر المطلوب في الرسالة.")
        return
    await asyncio.sleep(4)
    msg1 = await client.get_messages(bot_username, limit=1)
    if msg1[0].buttons and len(msg1[0].buttons) > 0:
        await msg1[0].click(0)
    else:
        await event.reply("لم يتم العثور على الزر المطلوب في الرسالة.")
        return

    chs = 1
    for i in range(100):
        if not collecting.get(event.sender_id, False):
            await event.reply("تم إيقاف التجميع ⛔")
            break
        await asyncio.sleep(4)
        history = await client.get_messages(bot_username, limit=1)
        msgs = history[0]
        if 'لا يوجد قنوات في الوقت الحالي' in msgs.message:
            await client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        if msgs.reply_markup and msgs.reply_markup.rows:
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await client(JoinChannelRequest(url))
                except:
                    invite_code = url.split('/')[-1]
                    await client(ImportChatInviteRequest(invite_code))
                msg2 = await client.get_messages(bot_username, limit=1)
                if msg2[0].buttons:
                    await msg2[0].click(text='تحقق')
                chs += 1
                await event.reply(f"تم الانضمام إلى {chs} قناة")
            except:
                msg2 = await client.get_messages(bot_username, limit=1)
                if msg2[0].buttons:
                    await msg2[0].click(text='التالي')
                chs += 1
                await event.reply(f"القناة رقم {chs}")
        else:
            await client.send_message(event.chat_id, "لا توجد أزرار في الرسالة، تم إيقاف التجميع.")
            break

@tgbot.on(events.CallbackQuery(data=b'tajme3_milyar'))
async def tajme3_milyar(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("📈 **سيتم تجميع النقاط من بوت المليار**")
        bot_username = '@EEObot'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@tgbot.on(events.CallbackQuery(data=b'tajme3_7rb'))
async def tajme3_7rb(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("📊 **سيتم تجميع النقاط من بوت اسيا سيل**")
        bot_username = '@yynnurybot'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@tgbot.on(events.CallbackQuery(data=b'tajme3_3qab'))
async def tajme3_3qab(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("🔥 **سيتم تجميع النقاط من بوت مهدوينو**")
        bot_username = '@MHDN313bot'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

@tgbot.on(events.CallbackQuery(data=b'tajme3_milyon'))
async def tajme3_milyon(event):
    if event.sender_id in user_sessions and "client" in user_sessions[event.sender_id]:
        client = user_sessions[event.sender_id]["client"]
        await event.reply("🏆 **سيتم تجميع النقاط من بوت ارشقلي**")
        bot_username = '@Ershkalibot'
        await join_channels(bot_username, event, client)
    else:
        await event.reply("الرجاء تسجيل الجلسة أولاً باستخدام زر تسجيل جلسة.")

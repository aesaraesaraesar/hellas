import requests
import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from JoKeRUB import l313l
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "البوت"

# إنشاء بريد وهمي
@l313l.l313l_cmd(pattern="بريد$")
async def create_temp_email(event):
    chat = "@TeMail_Robot"
    zed = await edit_or_reply(event, "**𓆰 جـار إنشـاء ايميـل وهمـي 📧...**")
    
    async with l313l.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("📧 Generate Email")
            await asyncio.sleep(5)
            response = await conv.get_response()
            email_text = response.text
            
            if "📧 Your temporary email" in email_text:
                email_msg = email_text.replace(
                    "📧 Your temporary email address:", 
                    "**𓆰 تم انشـاء Email وهمـي بنجـاح ☑️\n𓆰 الإيمـيل الوهمـي الخـاص بك هـو 📧 :**"
                )
                await zed.delete()
                await l313l.send_message(event.chat_id, email_msg)
        except YouBlockedUserError:
            await l313l(unblock("TeMail_Robot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("📧 Generate Email")
            await asyncio.sleep(5)
            response = await conv.get_response()
            email_text = response.text
            
            if "📧 Your temporary email" in email_text:
                email_msg = email_text.replace(
                    "📧 Your temporary email address:", 
                    "**𓆰 تم انشـاء Email وهمـي بنجـاح ☑️\n𓆰 الإيمـيل الوهمـي الخـاص بك هـو 📧 :**"
                )
                await zed.delete()
                await l313l.send_message(event.chat_id, email_msg)


# جلب البريد الوارد
@l313l.l313l_cmd(pattern="الوارد$")
async def get_inbox(event):
    chat = "@TeMail_Robot"
    zed = await edit_or_reply(event, "**𓆰 جـار جلب رسائـل البريـد 📬...**")

    async with l313l.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("📫 تحقق من OTP")
            await asyncio.sleep(5)
            response = await conv.get_response()
            inbox_text = response.text
            
            if "❌ No OTP" in inbox_text:
                inbox_msg = inbox_text.replace(
                    "❌ لم يتم استلام OTP...", 
                    "**𓆰 لا يوجـد رسـالة واردة لبريـدك الوهمـي بعـد 📭❌**"
                )
                await zed.delete()
                return await l313l.send_message(event.chat_id, inbox_msg)

            if "📬 Inbox" in inbox_text:
                await zed.delete()
                return await l313l.send_message(event.chat_id, f"**{inbox_text}**\n\n───────────────────\n𝗝𝗢𝗞𝗘𝗥𝗨𝗕 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\tmail • البـريد الـوارد")
            
            await zed.delete()
            await l313l.send_message(event.chat_id, f"**{inbox_text}**\n\n───────────────────\n𝗝𝗢𝗞𝗘𝗥𝗨𝗕 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\tmail • البـريد الـوارد")
        
        except YouBlockedUserError:
            await l313l(unblock("TeMail_Robot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("📫 تحقق من OTP")
            await asyncio.sleep(5)
            response = await conv.get_response()
            inbox_text = response.text
            
            if "❌ No OTP" in inbox_text:
                inbox_msg = inbox_text.replace(
                    "❌ لم يتم استلام OTP...", 
                    "**𓆰 لا يوجـد رسـالة واردة لبريـدك الوهمـي بعـد 📭❌**"
                )
                await zed.delete()
                return await l313l.send_message(event.chat_id, inbox_msg)

            if "📬 Inbox" in inbox_text:
                await zed.delete()
                return await l313l.send_message(event.chat_id, f"**{inbox_text}**\n\n───────────────────\n𝗝𝗢𝗞𝗘𝗥𝗨𝗕 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\tmail • البـريد الـوارد")
            
            await zed.delete()
            await l313l.send_message(event.chat_id, f"**{inbox_text}**\n\n───────────────────\n𝗝𝗢𝗞𝗘𝗥𝗨𝗕 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\tmail • البـريد الـوارد")

from JoKeRUB import l313l

# إعداد البوت
bot = l313l()

@bot.on_message()
def report_handler(message):
    if not message.text.startswith(".بلاغ"):
        return
    
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chat_id = message.chat.id
    
    args = message.text.split(" ", 2)
    if len(args) < 3:
        return bot.send_message(chat_id, "يجب عليك الرد على رسالة أو كتابة الرابط وتحديد نوع البلاغ وعدد البلاغات.")
    
    report_type = args[1] if len(args) > 1 else "غير محدد"
    report_count = args[2] if len(args) > 2 and args[2].isdigit() else "1"
    
    if message.reply_to_message:
        reported_message = message.reply_to_message
        message_link = f"https://t.me/c/{str(chat_id).replace('-100', '')}/{reported_message.message_id}"
    else:
        message_link = args[2] if len(args) > 2 and args[2].startswith("https://t.me/") else "رابط غير متوفر"
    
    report_text = f"🚨 *بلاغ جديد*\n"
    report_text += f"👤 المرسل: [{user_name}](tg://user?id={user_id})\n"
    report_text += f"🆔 معرفه: `{user_id}`\n"
    report_text += f"📜 نوع البلاغ: {report_type}\n"
    report_text += f"📢 عدد البلاغات: {report_count}\n"
    report_text += f"🔗 [رابط الرسالة]({message_link})\n"
    
    bot.send_message(chat_id, "✅ تم إرسال البلاغ بنجاح.")

bot.run()

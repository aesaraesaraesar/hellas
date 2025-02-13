from JoKeRUB import l313l

@l313l.on_message(l313l.filters.command("ضيف", prefixes="."))
def add_members(client, message):
    if len(message.command) < 2:
        message.reply("يرجى إدخال رابط المجموعة بعد الأمر.")
        return
    
    group_link = message.command[1]
    try:
        group = client.get_chat(group_link)
        contacts = client.get_contacts()
        
        for contact in contacts:
            try:
                client.add_chat_members(group.id, contact.user_id)
            except Exception as e:
                message.reply(f"تعذر إضافة {contact.user_id}: {str(e)}")
        
        message.reply("تمت إضافة الأعضاء بنجاح!")
    except Exception as e:
        message.reply(f"حدث خطأ: {str(e)}")

@l313l.on_message(l313l.filters.command("ضيف_جهاتي", prefixes="."))
def add_contacts(client, message):
    if not message.chat or not message.chat.id:
        message.reply("يجب إرسال الأمر داخل مجموعة.")
        return
    
    group_id = message.chat.id
    contacts = client.get_contacts()
    
    for contact in contacts:
        try:
            client.add_chat_members(group_id, contact.user_id)
        except Exception as e:
            message.reply(f"تعذر إضافة {contact.user_id}: {str(e)}")
    
    message.reply("تمت إضافة جميع جهات الاتصال بنجاح!")

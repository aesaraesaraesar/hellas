from telethon import events
from JoKeRUB import l313l, bot  # استدعاء البوت من السورس

VIRUSTOTAL_API_KEY = "d851c6064844b30083483cbfa5a2001d9ac0b811a666f0110c0efb4eaabf747e"

@bot.on(events.NewMessage(pattern=r"^\.افحص \+$"))
async def check_url(event):
    if not event.reply_to or not event.reply_to.message:
        await event.reply("❌ يرجى الرد على رسالة تحتوي على رابط ثم كتابة `.افحص +`.")
        return

    url = event.reply_to.message.message.strip()

    if not url.startswith(('http://', 'https://')):
        await event.reply("❌ الرابط غير صالح، تأكد أنه يبدأ بـ **http:// أو https://**.")
        return

    try:
        post_response = l313l.post(
            "https://www.virustotal.com/api/v3/urls",
            headers={"x-apikey": VIRUSTOTAL_API_KEY},
            data={"url": url}
        )

        if post_response.status_code == 200:
            url_id = post_response.json()['data']['id']
            response = l313l.get(
                f"https://www.virustotal.com/api/v3/analyses/{url_id}",
                headers={"x-apikey": VIRUSTOTAL_API_KEY}
            )

            if response.status_code == 200:
                data = response.json()
                analysis_stats = data['data']['attributes']['stats']
                result_message = (
                    f"🔍 **نتائج الفحص:**\n\n"
                    f"✅ آمن: {analysis_stats['harmless']}\n"
                    f"⚠ مشبوه: {analysis_stats['suspicious']}\n"
                    f"❌ ضار: {analysis_stats['malicious']}\n"
                )
                await event.reply(result_message)
            else:
                await event.reply("⚠ حدث خطأ أثناء استرجاع نتائج الفحص.")
        else:
            await event.reply("⚠ لم يتمكن البوت من إرسال الرابط إلى الفحص. حاول مرة أخرى.")

    except Exception as e:
        await event.reply(f"❌ خطأ غير متوقع: {e}")

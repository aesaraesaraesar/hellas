from gtts import gTTS
import os
from JoKeRUB import l313l

@l313l.on("انطق (.*)")
async def _(event):
    text = event.matches[0]

    if not text.strip():
        await event.reply("❌ يرجى إدخال نص للنطق.")
        return

    await event.reply("🗣️ جاري نطق: " + text)

    try:
        # تحويل النص إلى صوت
        tts = gTTS(text, lang="ar")
        file_path = "output_ar.mp3"
        tts.save(file_path)

        await event.reply("🎧 جاري إرسال الصوت...")

        # إرسال الملف الصوتي كبصمة
        async with event.client.action(event.chat_id, "record-voice"):
            await event.client.send_file(event.chat_id, file_path, voice_note=True)

        # حذف الملف بعد الإرسال
        os.remove(file_path)

    except Exception as e:
        await event.reply(f"❌ حدث خطأ: {str(e)}")

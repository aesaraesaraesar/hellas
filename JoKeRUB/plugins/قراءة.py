from telethon import TelegramClient, events
from telethon.tl.functions.channels import LeaveChannelRequest
from JoKeRUB import l313l
from ..Config import Config
import pytesseract
from PIL import Image
import os

plugin_category = "البوت"

# إذا كنت على ويندوز، حدد مسار Tesseract:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@l313l.on(events.NewMessage(pattern=".قراءة", incoming=True))
async def ocr_from_image(event):
    if not event.photo:
        await event.reply("❌ يرجى إرسال صورة مع الأمر.")
        return

    sender = await event.get_sender()
    photo = await event.download_media()

    try:
        # فتح الصورة ومعالجتها
        image = Image.open(photo)
        text = pytesseract.image_to_string(image, lang="ara+eng")  # يدعم العربية والإنجليزية

        if text.strip():
            await event.reply(f"📜 النص المستخرج:\n{text}")
        else:
            await event.reply("❌ لم يتم العثور على نص في الصورة.")

    except Exception as e:
        await event.reply(f"❌ حدث خطأ أثناء استخراج النص: {str(e)}")

    finally:
        # حذف الصورة بعد معالجتها لتوفير المساحة
        os.remove(photo)

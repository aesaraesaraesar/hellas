
import telebot
from telebot import types
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import io
import numpy as np
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_float
from JoKeRUB import l313l  # تم الاستيراد

bot = telebot.TeleBot("", parse_mode=None)  # إزالة التوكن ليعمل بأي دردشة
original_images = {}

@bot.message_handler(commands=['اوامر_الصور'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا بك في بوت تحسين الصور! أرسل صورة لبدء التعديل.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    image = Image.open(io.BytesIO(downloaded_file))
    
    user_id = message.from_user.id
    original_images[user_id] = image
    
    markup = types.InlineKeyboardMarkup()
    btn_enhance = types.InlineKeyboardButton("✨ تحسين الصورة", callback_data="enhance")
    btn_l313l = types.InlineKeyboardButton("⚡ استخدام l313l", callback_data="use_l313l")
    markup.add(btn_enhance, btn_l313l)
    
    bot.reply_to(message, "🖼 تم استلام الصورة! اختر عملية التعديل:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["enhance", "use_l313l"])
def handle_callback(call):
    user_id = call.from_user.id
    if user_id not in original_images:
        bot.answer_callback_query(call.id, "الرجاء إرسال صورة أولاً!")
        return
    
    image = original_images[user_id]
    
    if call.data == "enhance":
        image = enhance_image(image)
        caption = "✨ تم تحسين الصورة!"
    elif call.data == "use_l313l":
        image = l313l(image)  # تنفيذ دالة l313l على الصورة
        caption = "⚡ تم تطبيق l313l على الصورة!"
    
    bio = io.BytesIO()
    bio.name = 'edited.jpeg'
    image.save(bio, 'JPEG')
    bio.seek(0)
    
    bot.send_photo(call.message.chat.id, bio, caption=caption)
    bot.answer_callback_query(call.id)

def enhance_image(image):
    image = ImageEnhance.Sharpness(image).enhance(1.5)
    image = ImageEnhance.Contrast(image).enhance(1.3)
    image = ImageEnhance.Color(image).enhance(1.2)
    return image

bot.infinity_polling()

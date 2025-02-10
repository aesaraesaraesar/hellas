from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from youtube_search import YoutubeSearch
from pytube import YouTube
import os
from JoKeRUB import l313l

async def search_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text
        if text.lower().startswith("يوتيوب "):  # تغيير كلمة البحث لـ "يوتيوب + اسم الفيديو"
            query = text.replace("يوتيوب ", "").strip()
            if not query:
                await update.message.reply_text("يرجى إدخال اسم الفيديو بعد 'يوتيوب'.")
                return

            # استخدام l313l لتعديل النص إذا كان ذلك مناسبًا
            query = l313l(query)  # افترض أن l313l تعمل على تعديل النص أو إضافة شيء إليه

            results = YoutubeSearch(query, max_results=5).to_dict()
            if not results:
                await update.message.reply_text("لم أتمكن من العثور على أي نتائج.")
                return

            keyboard = []
            for result in results:
                video_title = result['title']
                video_url = f"https://www.youtube.com/watch?v={result['id']}"
                keyboard.append([InlineKeyboardButton(video_title, callback_data=video_url)])

            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text("اختر الفيديو لتحميله:", reply_markup=reply_markup)
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ أثناء البحث: {str(e)}")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        query = update.callback_query
        await query.answer()
        video_url = query.data
        await query.edit_message_text(text=f"جارٍ تحميل الفيديو من: {video_url}")

        yt = YouTube(video_url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        
        if not stream:
            await query.edit_message_text("لم أتمكن من العثور على تدفق مناسب للفيديو.")
            return

        file_path = stream.download()

        with open(file_path, 'rb') as video_file:
            await query.message.reply_video(video=video_file)

        os.remove(file_path)
    except Exception as e:
        await query.edit_message_text(f"حدث خطأ أثناء تحميل الفيديو: {str(e)}")

def main():
    # استخدام التوكن من خلال ملف بيئة أو إعدادات خاصة بدلاً من وضعه هنا بشكل صريح.
    application = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_video))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()

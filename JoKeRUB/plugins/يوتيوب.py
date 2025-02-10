from youtube_search import YoutubeSearch
from pytube import YouTube
import os
from JoKeRUB import l313l  # استيراد المكتبة المطلوبة

def search_video(query):
    """يبحث عن الفيديوهات في يوتيوب ويعرض النتائج."""
    results = YoutubeSearch(query, max_results=5).to_dict()
    if not results:
        print("❌ لم يتم العثور على نتائج.")
        return []

    videos = []
    for result in results:
        video_title = result['title']
        video_url = f"https://www.youtube.com/watch?v={result['id']}"
        videos.append((video_title, video_url))
    
    return videos

def download_video(video_url):
    """يقوم بتحميل الفيديو."""
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    file_path = stream.download()
    print(f"✅ تم تحميل الفيديو: {file_path}")
    return file_path

def main():
    """يعمل البرنامج بشكل دائم لالتقاط الرسائل."""
    print("✅ البرنامج يعمل... اكتب 'يوتيوب  + اسم الأغنية' للبحث.")
    while True:
        text = input("👤 أنت: ")
        if text.lower().startswith("يوتيوب  "):
            query = text.replace("يوتيوب  ", "").strip()
            if not query:
                print("⚠️ يرجى إدخال اسم الفيديو بعد 'يوتيوب بحث'.")
                continue

            videos = search_video(query)
            if videos:
                print("🎵 النتائج:")
                for i, (title, url) in enumerate(videos, 1):
                    print(f"{i}. {title} - {url}")

                choice = input("🔽 أدخل رقم الفيديو لتحميله أو اضغط Enter للخروج: ")
                if choice.isdigit() and 1 <= int(choice) <= len(videos):
                    download_video(videos[int(choice) - 1][1])
                else:
                    print("❌ لم يتم اختيار أي فيديو.")

if __name__ == "__main__":
    main()

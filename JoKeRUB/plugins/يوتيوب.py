from youtube_search import YoutubeSearch
from pytube import YouTube
import os
from JoKeRUB import l313l 

def search_video(query):
    """يبحث عن الفيديوهات في يوتيوب ويعرض النتائج."""
    results = YoutubeSearch(query, max_results=5).to_dict()
    if not results:
        print("❌ لم يتم العثور على نتائج.")
        return []

    return [(result['title'], f"https://www.youtube.com/watch?v={result['id']}") for result in results]

def download_video(video_url):
    """يقوم بتحميل الفيديو."""
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    file_path = stream.download()
    print(f"✅ تم تحميل الفيديو: {file_path}")

def main():
    """يعمل البرنامج بشكل دائم لالتقاط الرسائل."""
    print("✅ البرنامج يعمل... اكتب 'يوتيوب + اسم الأغنية' للبحث.")

    while True:
        text = input("👤 أنت: ").strip()
        
        if text.lower().startswith("يوتيوب "):
            query = text[7:].strip()  # حذف "يوتيوب " من بداية النص
            if not query:
                print("⚠️ يرجى إدخال اسم الفيديو بعد 'يوتيوب'.")
                continue

            videos = search_video(query)
            if not videos:
                continue

            print("\n🎵 النتائج:")
            for i, (title, url) in enumerate(videos, 1):
                print(f"{i}. {title} - {url}")

            choice = input("\n🔽 أدخل رقم الفيديو لتحميله أو اضغط Enter للخروج: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(videos):
                download_video(videos[int(choice) - 1][1])
            else:
                print("❌ لم يتم اختيار أي فيديو.")

if __name__ == "__main__":
    main()

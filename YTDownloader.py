from pytube import YouTube


youtube_video_url =input("Enter the the link of video on YouTube:")

try:
    yt_obj = YouTube(youtube_video_url)

    yt_obj.streams.get_audio_only().download(output_path='/Users/anjan/Desktop/Android Studio', filename='audio')
    print('YouTube video audio downloaded successfully')
except Exception as e:
    print(e)
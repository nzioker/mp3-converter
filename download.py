import yt_dlp as youtube_dl


def download_youtube_link_mp3(youtube_url):
    audio_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(audio_options) as ins:
            ins.download([youtube_url])
    except Exception as err:
        print("Pass in a Video link")



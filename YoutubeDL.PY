
from yt_dlp import YoutubeDL

def download_movie_trailer(SONG_name):
    search_query = f"ytsearch1:{SONG_name} Official PLAYLIST SONG"

    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s'
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_query, download=True)
        filename = ydl.prepare_filename(info['entries'][0])
    
    print(f"✅ डाउनलोड पूरा हुआ: {filename}")

if __name__ == "__main__":
    SONG_name = input("Enter song name (old or new): ")
    download_movie_trailer(SONG_name) # type: ignore
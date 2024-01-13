from pytube import YouTube
import winsound
from pytube import Playlist

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second

def on_progress_callback(stream, chunk, remaining):
    progress = (1 - remaining / stream.filesize) * 100
    print(f"Downloading... {progress:.2f}% complete")
        
def download(link):
    youtubeObject = YouTube(link, on_progress_callback=on_progress_callback)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except Exception  as e:
        print("An error has occurred", e)
    print("Download is completed successfully")
    winsound.Beep(frequency, duration)


def downloadPlaylist():
    playlist = input("Enter the YouTube playlist URL: ")
    p = Playlist(playlist)
    for url in p.video_urls:
        print(url)
        download(url)
        
def downloadVideo():
    video = input("Enter YouTube video URL: ")
    download(video)

# start
downloadPlaylist()
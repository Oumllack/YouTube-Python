from pytube import YouTube

url = input("Web link of the video: ")
def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent =  bytes_downloaded * 100 / stream.filesize
    print( f"Downloading: {int(percent)}%")


youtube_video = YouTube(url)
youtube_video.register_on_progress_callback(on_download_progress)
print("TITRE: " + youtube_video.title)

print("STREAMS")
for stream in youtube_video.fmt_streams:
    print(" ", stream)

stream = youtube_video.streams.get_by_itag(22)
print("Dowloading...")
stream.download()
print("DONE")
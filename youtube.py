from pytube import YouTube

def downlaodAudio(url):
    yt = YouTube(url)
    print(yt.title)
    audio = yt.streams.get_audio_only()
    audio.download()

def downloadVideo(url):
    yt = YouTube(url)
    print(yt.title)
    video = yt.streams.filter(resolution='720p', file_extension='mp4').first()
    video.download()

while True:
    print("Press '1' to download only audio")
    print("Press '2' to download video")
    print("Press '0' to exit")
    choice = input("Enter your choice: ")
    link = input("Enter youtube url: ")
    if choice == '1':
        downlaodAudio(link)
    elif choice == '2':
        downloadVideo(link)
    elif choice == '0':
        break
    else:
        print("Enter Valid Inputs!!")

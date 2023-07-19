# importing the module
from pytube import YouTube

link = "https://www.youtube.com/watch?v=wBdRWkDehQI"

yt = YouTube(link)

print(yt.title)

yt.streams.filter(resolution='720p', file_extension='mp4').first().download()

yt.streams.get_audio_only('mp4').download()

# d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
# d_video.download()


# try:
# downloading the video
# except:
#     print("Some Error!")
# print('Task Completed!')


# from pytube import YouTube

# url = "https://www.youtube.com/watch?v=xWOoBJUqlbI"
# my_video = YouTube(url)

# # Video Title
# print(my_video.title)

# # thumbnail url
# print(my_video.thumbnail_url)

# video = my_video.streams.all()
# # print(video)
# # vid = list(enumerate(video))
# # for i in vid:
# #     print(i)
# # print()
# for i, stream in enumerate(video):
#     print(f"{i}:{stream}")
# # strm = int("Enter: ")
# # video[strm].download()
# # print("Successfully Downloaded")

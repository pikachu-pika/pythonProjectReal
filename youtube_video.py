from pytube import YouTube

url="https://www.youtube.com/watch?v=RnBT9uUYb1w"
my_video=YouTube(url)

print("VIDEO TITLE")
print(my_video.title)

print("THUMBNAIL IMAGE")
print(my_video.thumbnail_url)

print("DOWNLOAD VIDEO")

my_video=my_video.streams.get_highest_resolution()

# my_video=my_video.streams.first()  # same as above
#
# for streams in my_video.streams:
#     print(streams)

my_video.download()

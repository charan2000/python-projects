from pytube import YouTube
from sys import argv

save_path = "/home/charan/Downloads"

link = argv[1]

# link = "youtube.com/watch?v=LXb3EKWsInQ"

yt = YouTube(link)

print(yt.title)
print(yt.views)


download = yt.streams.get_by_itag(303)

print(round(((download.filesize)/1024)/1024,2))
download.download(save_path)
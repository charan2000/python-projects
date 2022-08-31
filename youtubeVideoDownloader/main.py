from pytube import YouTube
# from sys import argv

save_path = "/home/charan/Downloads"

# link = argv[1]

link = "https://youtu.be/luDxcw7dsUM"

yt = YouTube(link)

print(yt.title)
print(yt.views)

down = yt.streams.get_by_itag(303)

# print(round((download.filesize / 1024) / 1024, 2))
down.download(save_path)

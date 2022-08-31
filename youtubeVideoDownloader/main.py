from pytube import YouTube
# from sys import argv

save_path = "/home/charan/Downloads"

# link = argv[1]

link = "https://www.youtube.com/watch?v=luDxcw7dsUM"
yt = YouTube(link)

print(yt.title)
print(yt.views)

down = yt.streams.get_highest_resolution()
print(down)
# print(round((down.filesize / 1024) / 1024, 2))
down.download(save_path,"NewVid")

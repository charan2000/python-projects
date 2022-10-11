import sys
from sys import argv
from pytube import YouTube

# from sys import argv

save_path = "/home/charlos/Downloads/"

link = argv[1]
# print(link)
# link = "https://www.youtube.com/watch?v=LXb3EKWsInQ&t=45s"
yt = YouTube(link)

# print(yt.streams.get_highest_resolution())
# print(yt.streams.all)
# down = yt.streams.get_by_itag("")

full_hd_60 = yt.streams.filter(resolution="1080p", mime_type="video/mp4", fps=60)[0]
full_hd = yt.streams.filter(resolution="1080p", mime_type="video/mp4")[0]
hd_60 = yt.streams.filter(resolution="720p", mime_type="video/mp4", fps=60)[0]
highest_res = yt.streams.get_highest_resolution()

if full_hd_60:
    codex = full_hd_60
elif full_hd:
    codex = full_hd
elif hd_60:
    codex = hd_60
else:
    codex = highest_res

codex = yt.streams.filter(resolution="1080p", mime_type="video/mp4", fps=60)[0]
codex_audio = yt.streams.filter(abr="128kbps", mime_type="audio/mp4")[0]
save_path = save_path + yt.title[:10]
print("THe Downloaded Files are saved in this path: " + save_path)
print(codex)
print(codex_audio)

codex.download(save_path, filename=yt.title[:10])
codex_audio.download(save_path, filename=yt.title[:10] + "Audio file")

sys.exit()

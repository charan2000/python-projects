from pytube import YouTube

# from sys import argv

save_path = "/home/charlos/Downloads/"

# link = argv[1]

link = "https://www.youtube.com/watch?v=IPdPUCbnEzs"
yt = YouTube(link)

print(yt.title)
print(yt.views)

print(yt.streams.get_highest_resolution())
print(yt.streams.all)
# down = yt.streams.get_by_itag("")
found = True
full_hd_60 = yt.streams.filter(resolution="1080p", mime_type="video/mp4", fps=60)[0]
full_hd = codex = yt.streams.filter(resolution="1080p", mime_type="video/mp4")[0]
hd_60 = yt.streams.filter(resolution="720p", mime_type="video/mp4", fps=60)[0]
highest_res = yt.streams.get_highest_resolution()
#
if full_hd_60:
    codex = full_hd_60
elif full_hd:
    codex = full_hd
elif hd_60:
    codex = hd_60
else:
    codex = highest_res

print(codex)
codex.download(save_path, filename=yt.title[:15])

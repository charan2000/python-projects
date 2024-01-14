import sys, os
from pathlib import Path
from pytube import YouTube

# from sys import argv

save_path = "downloads"

# link = argv[1]
# print(link)
link = "https://www.youtube.com/watch?v=esjBig0g-Gc"
yt = YouTube(link)
download_path = str(Path.home()/"Downloads")
# video = yt.streams.get_highest_resolution()
# video = yt.streams.filter(file_extension='mp4')
# print(yt.streams.filter(resolution="1080p", mime_type="video/mp4"))
# yt.streams.get_highest_resolution().
itag_no = yt.streams.filter(resolution="1080p", mime_type="video/mp4")[0].itag
video = yt.streams.get_by_itag(itag_no)
# print(list(yt.streams.filter(file_extension='mp4')))
video.download(output_path=download_path)

print("Downloaded : ")


# print(yt.streams.get_highest_resolution())
# print(yt.streams.all)
# down = yt.streams.get_by_itag("")

# print(full_hd_60)
# lst = full_hd_60.all()
# print(lst[0].itag)
# full_hd_60.download(output_path=save_path, filename="download_video")

# full_hd = yt.streams.filter(resolution="1080p", mime_type="video/mp4")[0]
# print(full_hd)
# hd_60 = yt.streams.filter(resolution="720p", mime_type="video/mp4", fps=60)[0]
# highest_res = yt.streams.get_highest_resolution()

# if full_hd_60:
#     codex = full_hd_60
# elif full_h                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              m                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             d:
#     codex = full_hd
# elif hd_60:
#     codex = hd_60
# else:
#     codex = highest_res

# codex = yt.streams.filter(resolution="1080p", mime_type="video/mp4", fps=60)[0]
# codex_audio = yt.streams.filter(abr="128kbps", mime_type="audio/mp4")[0]
# save_path = save_path + yt.title[:10]
# print("THe Downloaded Files are saved in this path: " + save_path)
# print(codex)
# print(codex_audio)

# codex.download(save_path, filename=yt.title[:10])
# codex_audio.download(save_path, filename=yt.title[:10] + "Audio file")

sys.exit()
playlist = "#EXTM3U\n"

with open("videos.txt") as f:
    for linha in f:
        nome, link = linha.strip().split("|")
        playlist += f"#EXTINF:-1,{nome}\n{link}\n"

with open("playlist.m3u","w") as f:
    f.write(playlist)

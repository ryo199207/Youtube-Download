from __future__ import unicode_literals
import youtube_dl

# Open text file
f=open('youtube-url.txt', 'r')
datas=f.readlines()

# Download execution line by line (youtube-download.py current directory)
for data in datas:
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([data])
        

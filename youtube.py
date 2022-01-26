# DOWNLOAD ANY VIDEO IN HIGH RESOLUTION FROM YOUTUBE


from pytube import YouTube
link=input("https://lnk.to/UnstoppableSia")
video=YouTube("https://lnk.to/UnstoppableSia")
stream = video.streams.get_highest_resoution()
stream.download()  
import pytube

video_url = 'https://www.youtube.com/watch?v=NUHj9E8PO6w'

youtube = pytube.YouTube(video_url)

video = youtube.streams.first()

video.download("Video/")

from moviepy.editor import *
video = VideoFileClip("output.avi")
audio = AudioFileClip("original.mp4")
audioAndVideo = video.set_audio(audio)
audioAndVideo.write_videofile("product.mp4")
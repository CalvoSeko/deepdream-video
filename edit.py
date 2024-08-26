from moviepy.editor import *
video = VideoFileClip("output.avi")
audio = AudioFileClip("original.mp4")
video.write_videofile("product.mp4")
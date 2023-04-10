#script-cut-video.py
from moviepy.editor import VideoFileClip

input_video = VideoFileClip ("office.mp4")

final_clip = input_video.subclip(0, 10)

final_clip.write_videofile("output.mp4", fps=60)
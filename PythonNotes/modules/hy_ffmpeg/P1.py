import os
import subprocess
import imageio
import imageio_ffmpeg
import ffmpeg
import imageio

video_path = 'A.mp4'
video_reader = imageio.get_reader(video_path, 'ffmpeg')

frame_list = []
for i, frame in enumerate(video_reader):
    frame_list.append(frame)

imageio.mimsave('out.mp4', frame_list)

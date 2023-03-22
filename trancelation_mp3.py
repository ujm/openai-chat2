# 動画を音声に変換。

import ffmpeg 
import sys
import os

video_path = sys.argv[1]
filename = os.path.basename(video_path)
print(video_path)
print(filename)

# 入力 
stream = ffmpeg.input(video_path) 
#stream = ffmpeg.input(r"C:\Users\user\Desktop\python\test.webm") 
# 出力 
stream = ffmpeg.output(stream, 'output\\' + filename + '.mp3') 
#stream = ffmpeg.output(stream, 'test.mp3') 
# 実行 
ffmpeg.run(stream)
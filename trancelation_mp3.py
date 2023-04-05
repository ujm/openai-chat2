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
# 出力 
stream = ffmpeg.output(stream, 'output\\' + filename + '.mp3') 
# 実行 
ffmpeg.run(stream)
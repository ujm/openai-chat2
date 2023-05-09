import openai
import sys
import os

api_key = os.environ['OPENAI_API_KEY']

openai.api_key = api_key

sound_path = sys.argv[1]

audio_file= open(sound_path, "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript["text"]+"\n")
translation = transcript["text"]+"を日本語に訳して。"

conversation = [{"role": "system", "content": "日本語翻訳"}]
conversation.append({"role": "user", "content": translation})

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
print(completion.choices[0].message.content.replace("。", "。\n"))

import openai
import os

api_key = "Your OpenAI-API-KEY"

openai.api_key = api_key
print('AI とのチャットの始まりです。[終了するには \"...\" を入力してください。]\n\n')
message = {"role":"user", "content":""}
conversation = [{"role": "system", "content": "日本語として回答して"}]

while(message["content"]!="bye"):
    message = {"role":"user", "content": input("あなた:")};
    conversation.append(message)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
    print("アシスタント: "+completion.choices[0].message.content+"\n\n")
    conversation.append(completion.choices[0].message)
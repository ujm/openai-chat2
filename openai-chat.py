import openai
import os

api_key = os.environ['OPENAI_API_KEY']

openai.api_key = api_key

print('[終了するには \"bye\" と入力してください。]\n\n')
message = {"role":"user", "content":""}
conversation = [{"role": "system", "content": "日本語として回答して"}]

while(message["content"]!="bye"):
    input_str = ""
    while True:
        if input_str == "":
            line = input('あなた: ')
        else:
            line = input('>>>')
        if line == "":
            break
        input_str += line + "\n"
    # 最後の改行を削除
    input_str = input_str.rstrip('\n')

    message = {"role":"user", "content":input_str};
    conversation.append(message)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
    print("アシスタント: "+completion.choices[0].message.content+"\n\n")
    conversation.append(completion.choices[0].message)

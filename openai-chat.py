import openai
import os
import time

api_key = os.environ['OPENAI_API_KEY']

openai.api_key = api_key

print('[終了するには \"bye\" と入力してください。]\n\n')
message = {"role":"user", "content":""}
conversation = [{"role": "system", "content": "システムエンジニア, 日本語, 手順を説明"}]

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

    while True:
        try:
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
            break
        except:
            time.sleep(5)
            print('処理中...')
            continue

    print(f"アシスタント: {completion.choices[0].message.content}\n")
    conversation.append(completion.choices[0].message)

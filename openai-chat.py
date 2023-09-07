import openai
import os
import time
import pickle

print('[終了するには \"ctrl+c\" と入力してください。]\n\n')
message = {"role":"user", "content":""}
conversation = [{"role": "system", "content": "ジャービスは優秀な執事です。返答は日本語で行います。"}]

while True:
    input_str = ""
    while True:
        if input_str == "":
            line = input('あなた: ')
        else:
            line = input('>>>')
        if line == "...":
            break
        input_str += line + "\n"
    # 最後の改行を削除
    input_str = input_str.rstrip('\n')

    message = {"role":"user", "content":input_str};
    conversation.append(message)

    while True:
        try:
            completion = openai.ChatCompletion.create(model="ft:gpt-3.5-turbo-0613:personal::7qh0GGa8", messages=conversation)
            break
        except:
            time.sleep(5)
            print('処理中...')
            continue

    if(len(conversation)==2):
        with open('my_array.pickle', 'wb') as f:
            pickle.dump(conversation, f)

    print(len(conversation))
    print(f"アシスタント: {completion.choices[0].message.content}\n")
    
    if(completion.usage.total_tokens == 4097) :
        del conversation[0]
        
    conversation.append(completion.choices[0].message)

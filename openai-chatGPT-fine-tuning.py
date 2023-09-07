import openai
import os
import time
import pickle

MODEL_NAME = "ft:gpt-3.5-turbo-0613:personal::7vLG90yA"
SLEEP_INTERVAL = 5
PICKLE_FILE = 'my_array.pickle'
PROMPT = 'あなた: '
CONTINUE_PROMPT = '>>>'
ERROR_MESSAGE = '処理中...'
EXIT_MESSAGE = '[終了するには "ctrl+c" と入力してください。]\n\n'

print(EXIT_MESSAGE)

message = {"role":"user", "content":""}
conversation = [{"role": "system", "content": "You are an assistant specialized in crafting business emails with the user's specific style."}]

while True:
    input_str = ""

    while True:
        line = input(PROMPT if input_str == "" else CONTINUE_PROMPT)
        if line == "...":
            break
        input_str += line + "\n"

    # 最後の改行を削除
    input_str = input_str.rstrip('\n')

    message = {"role":"user", "content":input_str}
    conversation.append(message)

    while True:
        try:
            completion = openai.ChatCompletion.create(model=MODEL_NAME, messages=conversation)
            break
        except openai.error.OpenAIError:
            print(ERROR_MESSAGE)
            time.sleep(SLEEP_INTERVAL)

    with open(PICKLE_FILE, 'wb') as f:
        pickle.dump(conversation, f)

    print(f"アシスタント: {completion.choices[0].message.content}\n")
    conversation.append(completion.choices[0].message)

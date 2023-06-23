import openai
import requests
import json

# OpenAIのAPIキーとGoogle Custom SearchのAPIキーおよび検索エンジンIDを設定
google_cse_key = 'AIzaSyB0Etkfab_dL3ZlhT370bFXb9F6R6nv3QM'
google_cse_id = 'e14a119c37f1441bd'

# Google Custom Search APIを呼び出す関数を定義
def perform_web_search(query):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': google_cse_key,
        'cx': google_cse_id,
        'q': query
    }
    response = requests.get(url, params=params)
    response_json = response.json()
    items = response_json.get('items', [])
    top_3_snippets = [item.get('snippet') for item in items[:3]]
    
    return top_3_snippets

def run_conversation():
    # Step 1: send the conversation and available functions to GPT
    messages=[{"role": "user", "content": '今日のニュース'}]
    functions=[
        {
            "name": "perform_web_search",
            "description": "messages の内容を検索します。",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query",
                    },
                },
            "required": ["query"],
            },
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )

    response_message = response["choices"][0]["message"]
    # Step 2: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "perform_web_search": perform_web_search,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            query=function_args.get("query"),
        )

        # Step 4: send the info on the function call and function response to GPT
        print(response_message)
        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": json.dumps(function_response),
            }
        )  # extend conversation with function response
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        return second_response
    else:
        return response["choices"][0]["message"]["content"]


print(run_conversation()["choices"][0]["message"]["content"])

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key = api_key,
                base_url = "https://genai.ghaymah.systems")

def read_code(path_of_file):
    try:
        with open(path_of_file, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return 'Error! file not found'
    except Exception as e:
        return f'Error reading file: {e}'

file_path = os.path.join("test", "example.py")
code_content = read_code(file_path)

print("The code is read, you can start asking about it\nType exit to exit")

message = [{
    "role": "system",
    "content": (
        "You are a concise and clear code assistant."
        "Your rules: "
        "1) Always return only the final answer. "
        "2) The answer must be short, clear, and sufficient. "
        "3) Never include your reasoning, steps, or filler words. "
        "4) Every response should directly address the user's request."
    )
},
{"role": "system",
 "content": f"The code is: \n{code_content}"}
]

while True:
    max_tokens = 100
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print('conversation ended')
        break

    message.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model = "DeepSeek-V3-0324",
        messages = message,
        max_tokens = max_tokens
    )

    reply = response.choices[0].message.content
    print("Bot:", reply)

    message.append({"role": "assistant", "content": reply})
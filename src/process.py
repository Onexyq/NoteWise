# HackSC 2023
# Authors: Boshe Zhang, Yiqi Xue, Zhiyuan Wang, Ying Sun

from cache import AsyncLRU
import openai
import json

with open("./keys/openai.key") as f: 
    openai.api_key = f.readline()

@AsyncLRU(maxsize=128)
async def get_mind_map(text_data):
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo-16k",
        temperature=0.2,
        messages=[
            {"role": "system", "content": "You are a helpful mindmap maker, you can summerize the text into a mindmap."},
            {"role": "user", "content": "Convert the following text into a mindmap, using markdown language, keep all key points"},
            {"role": "user", "content": text_data}
        ]
    )

    parsed_data = json.loads(json.dumps(response.choices[0].message))
    markdown_text = parsed_data['content']

    return markdown_text

@AsyncLRU(maxsize=128)
async def get_explanation(text_data):
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo-16k",
        temperature=0.2,
        messages=[
            {"role": "system", "content": "You are a helpful explainer, you can summerize the text and explain it using easy words."},
            {"role": "user", "content": "Explain the following text, keep all key points"},
            {"role": "user", "content": text_data}
        ]
    )

    parsed_data = json.loads(json.dumps(response.choices[0].message))
    text = parsed_data['content']

    return text

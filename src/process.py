# HackSC 2023
# Authors: Boshe Zhang, Yiqi Xue, Zhiyuan Zhang, Ying Sun

import openai
import json

with open("src/keys/openai.key") as f: 
    openai.api_key = f.readline()

def process_mindmap_data(text_data):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful mindmap maker, you can summerize the text into a mindmap."},
            {"role": "user", "content": "Convert the following text into a mindmap, using markdown language, keep all key points."},
            {"role": "user", "content": text_data}
        ]
    )

    parsed_data = json.loads(json.dumps(response.choices[0].message))
    markdown_text = parsed_data['content']

    return markdown_text


def process_notes_data(text_data):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful note taker, you can summerize the text into well-structured notes."},
            {"role": "user", "content": "Convert the following text into key notes, keeping all white spaces."},
            {"role": "user", "content": text_data}
        ]
    )

    parsed_data = json.loads(json.dumps(response.choices[0].message))
    markdown_text = parsed_data['content']

    return markdown_text


def process_slides_data(text_data):
    return
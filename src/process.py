#HackSC
#Authors: Boshe Zhang, Yiqi Xue, Zhiyuan Zhangm, Ying Sun

import openai
openai.api_key = ('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')

def process_data(text_data):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful mindmap maker, you can summerize the text into a mindmap."},
            {"role": "user", "content": "Convert the following text into a mindmap, using markdown language, keep all key points"},
            {"role": "user", "content": text_data}
        ]
    )

    markdown_text = response.choices[0].message

    return markdown_text


# def prompt():
#     openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful summerizer. "},
#             {"role": "user", "content": "Summarize the following in markdown format."},
#         ]
#     )
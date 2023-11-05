import openai

with open("src/keys/openai.key") as f: 
    openai.api_key = f.readline()

def process_data(text_data):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful notetaker, you can summerize the text into a mindmap."},
            {"role": "user", "content": "Convert the following text into a mindmap, using markdown language, keep all details and exteral url links."},
            {"role": "user", "content": text_data}
        ]
    )

    print(response.choices[0].message)

    return response.choices[0].message


import openai

with open("./keys/openai.key") as f:
    openai.api_key = f.readline()

def process_data(text_data):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful summerizer."},
            {"role": "user", "content": text_data},
        ]
    )

    print(response.choices[0].message)

    return response.choices[0].message


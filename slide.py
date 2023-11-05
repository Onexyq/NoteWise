import requests

payload={'jsonData': '{"template":"title_slide_template.pptx","export_version":"Pptx2010","resultFileName":"quick_start_example","slides":[{"type":"slide","slide_index":0,"shapes":[{"name":"Title 1","content":"Your generated PowerPoint presentation"},{"name":"Subtitle 2","content":"Create, fill and manage PowerPoint documents through simple API requests."}]}]}'}

files=[
  ('files', ('title_slide_template.pptx', open('./title_slide_template.pptx','rb'), 'application/vnd.openxmlformats-officedocument.presentationml.presentation'))
]


response = requests.post(
    'https://gen.powerpointgeneratorapi.com/v1.0/generator/create',
    data=payload,
    files=files,
    headers={
        'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYm9zaGVuemhAdXNjLmVkdSIsIm5iZiI6IjE2OTkxNzA0NzIiLCJleHAiOiIxNjk5MjU2ODcyIn0._clwsxbBFLEi3lpy_vHDhdUisvuiisQBpaR9Wp6Yrz0',
    },
    timeout=360
)
print(response.content)
with open("./generated.pptx", "wb") as file:
    file.write(response.content)
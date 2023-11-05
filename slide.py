import requests

jsonData = """{
   "presentation":{
      "template":"title_slide_template.pptx",
      "export_version":"Pptx2010",
      "resultFileName":"quick_start_example",
      "slides":[
         {
            "type":"slide",
            "slide_index":0,
            "shapes":[
               {
                  "name":"Title 1",
                  "content":"Your generated PowerPoint presentation"
               },
               {
                  "name":"Subtitle 2",
                  "content":"Create, fill and manage PowerPoint documents through simple API requests."
               }
            ]
         }
      ]
   }
}"""


jsonData2 = '{"presentation":{"template":"title_slide_template.pptx", "export_version":"Pptx2010", "resultFileName":"quick_start_example","slides":[{"role": "assistant", "content": "{"type":"slide","slide_index":0,"shapes":[{"name":"Machine Learning CSCI 567","content":"Your Name"},{"name":"About this course","content":"Modern machine learning methods used in real-world AI applications. Focus on conceptual understanding of these methods."},{"name":"Objectives","content":"Develop skills to grasp abstract ML concepts and think critically. Practice with hands on programming tasks. Preparation for studying more advanced machine learning techniques."},{"name":"Prerequisites","content":"Undergraduate level training in probability and statistics, linear algebra, (multivariate) calculus. Important: attend todayu2019s discussion session to see if you have the required background. Programming: Python. Not an intro-level CS course, no training of basic programming skills."},{"name":"Logistics","content":"Lectures: Fridays, 1-3.20pm (SGM 123) Discussions: Fridays, 3.30-4.20pm Course website: https://usc-tamagotchi.github.io/csci-567/23f/"},{"name":"Teaching Staff","content":"TAs: Ting-Rui Chiang, Samuel Griesemer, Josh Robinson, Oliver Liu, Robby Costales, Tenghao Huang, Tejas Srinivasan CPs/Graders: Aman Bansal, Wenda Zhou, Sanying Yi, Sneha Bandi"},{"name":"Slides and Reading","content":"Lecture slides will be posted before class (possibly updated after). No required textbooks."},{"name":"Grade","content":"25%: Quiz 1 (9/29). Open book, no collaboration. 25%: Quiz 2 (11/17). Open book, no collaboration. 50%: Course Project"},{"name":"Academic integrity","content":"Done in groups (~3 students). Any machine learning topic and any domain is fine. It must include an implementation of a machine learning algorithm. The implemented model has to work to a reasonable level (donu2019t pick a problem that is too difficult). We will share more details in a separate document early next week."},{"name":"What is machine learning?","content":"Machine learning is the fuel that powers state-of-the-art AI agents. It is used in various applications such as speech recognition, information retrieval, stock price prediction, and more."},{"name":"Why do we need to study ML?","content":"Understanding fundamental concepts of how ML models work. Developing strong engineering skills. Contributing to the rapid pace of progress in AI."},{"name":"How to train a model","content":"Learning a model from training data by optimizing a loss function to minimize generalization errors. Supervised learning involves mapping inputs to predicted outputs using available training data."},{"name":"Data","content":"Input data is often represented as a feature vector. Supervised learning involves learning a function that maps new inputs to predicted outputs."},{"name":"Model","content":"In supervised learning, the goal is to learn a function based on training data that can predict outputs for new inputs. Various models such as decision trees, k-nearest neighbors, and linear classifiers can be used."},{"name":"Loss function","content":"A loss function is used to measure the error between predicted outputs and actual outputs. The goal is to choose a function that minimizes generalization errors and is robust to noise in the training data."}]}"}]}}'

jsonData2 = jsonData2.replace("\\", "")

payload={'jsonData': jsonData2}

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
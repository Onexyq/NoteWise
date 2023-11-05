#HackSC 2023
#Authors: Boshe Zhang, Yiqi Xue, Zhiyuan Zhangm, Ying Sun


from gevent.pywsgi import WSGIServer
from flask import Flask, request
from flask_limiter import Limiter
from process import get_mind_map, get_explanation

# build flask app
app = Flask(__name__)

limiter = Limiter(
    app,
    default_limits=["5 per minute"],  # max 5 requests per minute
)



@app.route('/api/mindmap', methods=['POST'])
async def post_data():
    text_data = request.data.decode('utf-8') 
    print(text_data)   
    processed_data = await get_mind_map(text_data)
    print(processed_data)
    return processed_data



@app.route('/api/explain', methods=['POST'])
async def get_data():
    text_data = request.data.decode('utf-8')    
    processed_data = await get_explanation(text_data)
    print(processed_data)
    return processed_data


# entrance
if __name__ == '__main__':
    print("server started")
    http_server = WSGIServer(('0.0.0.0', 8080), app)
    http_server.serve_forever()

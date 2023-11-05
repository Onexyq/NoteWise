# HackSC 2023
# Authors: Boshe Zhang, Yiqi Xue, Zhiyuan Zhang, Ying Sun


from gevent.pywsgi import WSGIServer
from flask import Flask, request
from flask_limiter import Limiter
from process import *


# build flask app
app = Flask(__name__)

# limitation on max 5 requests per minute
limiter = Limiter(
    app,
    default_limits=["5 per minute"],  
)

# Mindmap Generation API
@app.route('/api/mindmap', methods=['POST'])
def post_mindmap_data():

    text_data = request.data.decode('utf-8')
    
    processed_data = process_mindmap_data(text_data)

    return processed_data

# Notes Generation API
@app.route('/api/notes', methods=['POST'])
def post_notes_data():

    text_data = request.data.decode('utf-8')
    
    processed_data = process_notes_data(text_data)

    return processed_data

# Slides Generation API
@app.route('/api/slides', methods=['POST'])
def post_slides_data():
    return



# program entrance
if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 8080), app)
    http_server.serve_forever()

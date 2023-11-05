#HackSC
#Authors: Boshe Zhang, Yiqi Xue, Zhiyuan Zhangm, Ying Sun
#

import time

from flask import Flask, request
from flask_limiter import Limiter
from process import process_data

# 创建Flask应用
app = Flask(__name__)

limiter = Limiter(
    app,
    default_limits=["5 per minute"],  # 每分钟最多允许 5 次请求
)


# 定义路由和视图函数
@app.route('/')
def hello_world():
    return 'Hello, World!'

# @app.route('/api/data', methods=['GET'])
# def get_data():
#     data = {
#         'message': 'Hello, this is a Flask API!',
#         'status': 'success'
#     }
#     return data


@app.route('/api/data', methods=['GET'])
def post_data():
    # 从请求中获取数据
    #data = request.get_json()
    
    #text_data = request.data.decode('utf-8')
    

    text_data = 'The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.'

    # # 检查是否有名为 'data' 的键
    # if 'data' in data:
    #     received_data = data['data']
    #     return jsonify({'message': 'Data received successfully', 'data': received_data})
    # else:
    #     return jsonify({'error': 'No "data" key in the request'})

    
    processed_data = process_data(text_data)

    return processed_data


# 运行应用
if __name__ == '__main__':
    app.run(debug=True)
    
    
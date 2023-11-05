from flask import Flask, request
from process import process_data

# 创建Flask应用
app = Flask(__name__)

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
    text_data = request.data.decode('utf-8')

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
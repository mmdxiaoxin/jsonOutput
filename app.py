from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/json-data', methods=['GET'])
def get_json_data():
    # 从本地JSON文件读取数据
    with open('D:/mycode/C++/virtual_studio/跳马/output.json', 'r') as file:
        json_data = file.read()

    # 设置响应头为JSON类型
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    return response


if __name__ == '__main__':
    app.run()

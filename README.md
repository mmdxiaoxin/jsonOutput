# 使用说明

本文档介绍了如何在 PyCharm 中使用 Flask 库创建一个简单的 Web 应用程序，该应用程序使用前端页面和后端接口来显示国际象棋中马的跳跃动画。前端页面使用 HTML、CSS 和 JavaScript，后端使用 Flask 框架来提供 JSON 数据。

## 环境配置

要在 PyCharm 中配置环境以运行该代码，需要按照以下步骤进行操作：

1. 安装 PyCharm：前往 PyCharm 官方网站，下载并安装适用于您的操作系统的 PyCharm 版本。

2. 创建项目：在 PyCharm 中创建一个新的 Python 项目。

3. 导入依赖库：在 PyCharm 的项目中，使用 `pip` 命令或 PyCharm 的包管理工具，安装 Flask 和 flask-cors 库。

4. 在 PyCharm 中，您可以使用以下命令来安装所需的依赖库：

   ```bash
   pip install -r requirements.txt
   ```

5. 将提供的代码文件添加到项目中：将给定的代码文件添加到项目中。代码文件包括 `app.py` 和 `static/ChessboardAnimation.html`。

完成上述步骤后，您的环境就已经配置好了，可以运行代码。

## 代码使用

在代码中，`app.py` 文件包含了 Flask 应用程序的后端逻辑，`static/index.html` 文件包含了前端页面的 HTML、CSS 和 JavaScript 代码。

### 后端代码

在 `app.py` 文件中，创建了一个 Flask 应用程序，并配置了跨域资源共享（CORS）以允许前端页面从不同的源访问后端接口。

应用程序定义了一个 `/json-data` 路由，当收到 GET 请求时，从本地的 JSON 文件中读取数据，并以 JSON 格式返回响应。

```python
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
```

### 前端代码

在 `static/index.html` 文件中，定义了一个包含棋盘的 HTML 结构，并使用 CSS 设置了棋盘格子的样式。

JavaScript 代码部分使用 `fetch` 函数发送 GET 请求获取后端返回的 JSON 数据。然后，根据 JSON 数据中的起始位置、目标位置和路径信息，动态生成棋盘格子，并实现马的跳跃动画。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>国际象棋马跳跃动画</title>
    <style>
        /* 在这里添加样式 */
        #chessboard {
            width: 100%;
            display: grid;
            grid-template-columns: repeat(var(--board-size), 20px);
            grid-template-rows: repeat(var(--board-size), 20px);
            gap: 0;
        }

        .cell {
            width: 20px;
            height: 20px;
            border: 1px solid #ccc;
        }

        .cell.white {
            background-color: #ffffff;
        }

        .cell.black {
            background-color: #000000;
        }

        .cell.yellow {
            background-color: #ffff00;
        }

        .cell.knight {
            background-color: red;
        }
    </style>
</head>
<body>
    <div id="chessboard"></div>
    <script>
        // 初始化棋盘
        const chessboard = document.getElementById('chessboard');

        // 发送GET请求获取JSON数据
        fetch('http://127.0.0.1:5000/json-data')
            .then(response => response.json())
            .then(data => {
                const boardSize = data.boardSize;
                const start = data.start;
                const target = data.target;
                const path = data.path;

                chessboard.style.setProperty('--board-size', boardSize);

                for (let i = 0; i < boardSize; i++) {
                    for (let j = 0; j < boardSize; j++) {
                        const cell = document.createElement('div');
                        cell.className = 'cell ' + ((i + j) % 2 === 0 ? 'white' : 'black');
                        cell.id = `cell-${i + 1}-${j + 1}`;
                        chessboard.appendChild(cell);
                    }
                }

                const startCell = document.getElementById(`cell-${start.x}-${start.y}`);
                startCell.innerText = 'S';
                startCell.className = 'cell yellow';
                const targetCell = document.getElementById(`cell-${target.x}-${target.y}`);
                targetCell.innerText = 'T';
                targetCell.className = 'cell yellow';

                // 马的跳跃动画
                const delay = 1000;

                function moveKnight(index) {
                    if (index >= path.length) return;

                    const position = path[index];
                    const currentCell = document.getElementById(`cell-${position.x}-${position.y}`);
                    console.log(position);

                    // 移除马图标
                    if (index > 0) {
                        const previousCell = document.getElementById(`cell-${path[index - 1].x}-${path[index - 1].y}`);
                        previousCell.classList.remove('knight');
                    }

                    // 添加马图标
                    currentCell.classList.add('knight');

                    // 递归调用
                    setTimeout(() => moveKnight(index + 1), delay);
                }

                moveKnight(0);
            })
            .catch(error => console.error('Error:', error));
    </script>
</body>
</html>
```

## 运行代码

在 PyCharm 中，打开 `app.py` 文件，并点击运行按钮来启动 Flask 应用程序。

在浏览器中访问 `http://127.0.0.1:5000`，即可看到马的跳跃动画在棋盘上展示出来。

请注意，确保在运行代码之前已经生成了 JSON 数据文件（`output.json`）并存放在正确的路径下（注：这里可以自定义使用）。

## 其他说明

- 本代码使用了 Flask 和 flask-cors 库，请确保已正确安装这些库。
- 如果出现任何错误，请检查您的环境配置和代码设置，并确保文件路径和端口号等设置正确。
- 如果您的代码和数据存放在不同的路径下，请根据实际情况修改代码中的文件路径。

希望这份文档能帮助您理解和使用代码。如果您有任何问题或需要进一步的帮助，请随时提问。
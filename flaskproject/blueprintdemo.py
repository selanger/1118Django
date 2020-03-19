from flask import Flask
from flask import Blueprint     ## Blueprint 不需要安装
app = Flask(__name__)
## 声明蓝图
## 第一个参数 为蓝图的名字
## 第二个参数   import name  传递 __name__ 即可，代表当前模块
bl = Blueprint("bl",__name__)

@app.route("/index/")
def index():
    return "index"

## 由bl 代替了部分的 app 的功能
@bl.route("/index/")
def index():
    return "bl_index"

## 注册蓝图
app.register_blueprint(bl,url_prefix="/bl")


if __name__ == '__main__':
    app.run(debug=True)






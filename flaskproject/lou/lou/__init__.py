## flask 项目的初始化文件
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
## 数据库的配置
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:111111@localhost/lou"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# app.config["SQLALCHEMY_ECHO"] = True

## 绑定app 和sqlalchemy
db = SQLAlchemy(app)



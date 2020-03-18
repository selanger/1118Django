## flask 项目的初始化文件
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import os
app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
## 数据库的配置
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:111111@localhost/lou"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# app.config["SQLALCHEMY_ECHO"] = True
# app.config.from_pyfile("settings.py")
# app.config.from_object("settings.Config")
app.config.from_object("settings.TestConfig")
app.config.from_envvar("FLASKCONFIG",silent=True)
## 绑定app 和sqlalchemy
db = SQLAlchemy(app)
STATICFILES_DIRS = os.path.join(BASE_DIR,'static')
app.config["STATICFILES_DIRS"] = os.path.join(BASE_DIR,'static')
app.config["SECRET_KEY"] = "dhfsdjkaf"
api = Api(app)



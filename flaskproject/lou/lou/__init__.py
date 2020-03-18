## flask 项目的初始化文件
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import os
app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config.from_object("settings.Config")
## 绑定app 和sqlalchemy
db = SQLAlchemy(app)
STATICFILES_DIRS = os.path.join(BASE_DIR,'static')

api = Api(app)



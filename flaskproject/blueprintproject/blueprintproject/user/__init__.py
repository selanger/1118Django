## 子应用的初始化文件

from flask import Blueprint
from flask_restful import Api

user_bl = Blueprint("user",__name__)
api=Api(user_bl)

from .models import *
from blueprintproject.user.views import *

## 子应用的初始化文件

from flask import Blueprint

user_bl = Blueprint("user",__name__)
# from user.views import *
from blueprintproject.user.views import *
from flask import Blueprint
from flask_restful import Api
# from course.views import *   ## 循环导包 出现错误
course_bl = Blueprint("course",__name__)
api = Api(course_bl)

# from course.views import *
from blueprintproject.course.views import *
api.add_resource(CoueseDemo,"/demo/")
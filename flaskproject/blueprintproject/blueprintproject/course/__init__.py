from flask import Blueprint
# from course.views import *   ## 循环导包 出现错误
course_bl = Blueprint("course",__name__)

# from course.views import *
from blueprintproject.course.views import *
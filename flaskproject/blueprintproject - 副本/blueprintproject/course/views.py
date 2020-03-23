# from course import course_bl
# from course.models import *
from blueprintproject.course import course_bl
from blueprintproject.course.models import *
from flask_restful import Resource

@course_bl.route("/index/")
def index():
    return "courseindex"
@course_bl.route("/add/")
def add():
    l = Label(name="xxxxx",description="xxxxxx")
    l.save()
    return "增加数据"


class CoueseDemo(Resource):
    def get(self):
        return "resource"
    def post(self):
        return "resource"
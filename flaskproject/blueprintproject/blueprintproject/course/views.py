# from course import course_bl
# from course.models import *
from blueprintproject.course import course_bl
from blueprintproject.course.models import *

@course_bl.route("/index/")
def index():
    return "courseindex"
@course_bl.route("/add/")
def add():
    l = Label(name="xxxxx",description="xxxxxx")
    l.save()
    return "增加数据"

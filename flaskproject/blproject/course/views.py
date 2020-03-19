from course import course_bl

@course_bl.route("/index/")
def index():
    return "course_index"


from course.models import *
@course_bl.route("/add/")
def add():
    c = Course(name="python")
    db.session.add(c)
    db.session.commit()
    return "增加数据"
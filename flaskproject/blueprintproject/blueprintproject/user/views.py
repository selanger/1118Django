## 视图
# from user import user_bl
from blueprintproject.user import user_bl


@user_bl.route("/index/")
def index():
    return "userindex"
## 视图
# from user import user_bl
from blueprintproject.user import user_bl
from flask_restful import Resource
from blueprintproject.user import api


@user_bl.route("/index/")
def index():
    return "userindex"

class Demo(Resource):
    def get(self):
        return "get"
    def post(self):
        return "post"

### 收集路由
# api.add_resource(Demo,"/demo/")

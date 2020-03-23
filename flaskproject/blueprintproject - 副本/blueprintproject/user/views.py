## 视图
# from user import user_bl
from blueprintproject.user import user_bl
from flask_restful import Resource
from blueprintproject.user import api
import functools
from flask import g,current_app

def LoginValid(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        ## 校验规则
        print(1111111)
        ## 可以获取请求中的 session 或者cookie
        ## 比如 cookie 中有一个 user_id
        # user_id = request.cookies.get("user_id")
        user_id = 1
        g.user_id = user_id
        return func(*args,**kwargs)
    return inner

@user_bl.route("/index/")
@LoginValid
def index():
    print("---------index----------")

    ## 也需要使用user_id
    # user_id = g.get("user_id")
    # print(user_id)
    ### 做加密  需要使用配置文件中的密钥串
    ## 1、 导入 app
    ## 2、 app.config.get("SECRET_KEY")
    # key = current_app.config.get("SECRET_KEY")
    # print(key)
    return "userindex"

class Demo(Resource):
    def get(self):
        return "get"
    def post(self):
        return "post"

### 收集路由
# api.add_resource(Demo,"/demo/")
from flask import render_template
from flask import request
from .forms import UserForm
@user_bl.route("/register/",methods = ["GET","POST"])
def register():
    userform = UserForm()
    if request.method == "POST":
        # data = request.form
        # print(data)
        if userform.validate_on_submit():     ### 后端校验
            ## True 代表校验通过
            print("通过")
            data = userform.data      #### 校验通过之后的值   类型是字典
            # print(data)
            name = data.get("name")
            password = data.get("password")
            ### 保存数据库
        else:
            ## false 代表校验失败、
            # print("失败")
            # print(userform.errors)    ### 校验失败之后的报错内容
            errors = userform.errors
    return render_template("register.html",**locals())

## 避免csrf校验
from blueprintproject import csrf
@user_bl.route("/registercsrf/",methods =["GET","POST"])
@csrf.exempt
def registercsrf():
    if request.method == "POST":
        data = request.form
        print(data)
    return render_template("registercsrfdemo.html")


from flask_wtf.csrf import generate_csrf
@user_bl.route("/getcsrftoken/")
def getcsrftoken():
    csrf_token = generate_csrf()
    return csrf_token








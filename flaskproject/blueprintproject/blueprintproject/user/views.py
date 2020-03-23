## 视图
from blueprintproject.user import user_bl
import functools
from flask import session,redirect,request,render_template
from .models import *

def LoginValid(func):
    @functools.wraps(func)     ### 保留原来的函数名
    def inner(*args,**kwargs):
        ## 校验是否登录
        cookie_name = request.cookies.get("name")
        session_name = session.get("name")
        if cookie_name and session_name and cookie_name == session_name:
            ## 登录
                ## 返回函数执行结果
            return func(*args,**kwargs)
        ## 未登录
        return redirect("/user/login/")
            ## 重定向到登录
        # return func(*args,**kwargs)
    return inner




@user_bl.route("/register/",methods=["GET","POST"])
def register():
    ## 通过post请求 获取参数
    ## 保存数据
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        email = request.form.get("email")
        if name and password:
            u = User(name=name,password=password,role_id=1)
            u.save()
            ## 注册成功重定向到 登录页面
            return redirect('/user/login/')
        else:
            message = "参数为空"
            return render_template("index.html",**locals())

    return render_template("index.html")


@user_bl.route("/login/",methods=["GET","POST"])
def login():
    flag = True
    ## 通过post请求获取数据  校验数据
    if request.method == "POST":
        print(request.form)
        name = request.form.get("name")
        password = request.form.get("password")
        if name and password:
            ## 校验数据
            user = User.query.filter(User.name==name,User.password==password).first()
            print(user)
            if user:
                ## 用户存在
                ## 重定向到课程页面
                # return redirect("/courses/")
                response = redirect('/course/courses/')
                response.set_cookie("name",name)
                session["name"] = name
                return response
            else:
                ## 用户不存在
                flag = True   ## 继续登录
                message = "用户名密码错误"
                return render_template("index.html",**locals())
        return  render_template("index.html",**locals())

    return render_template("index.html",**locals())

@user_bl.route("/logout/")
def logout():
    response = redirect("/login/")
    response.delete_cookie("name")
    del session["name"]
    return response






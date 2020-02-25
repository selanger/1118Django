from django.shortcuts import render
import hashlib
from django.http import HttpResponseRedirect
from Seller.models import LoginUser



# Create your views here.
## 密码加密
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result
## 登录装饰器
def loginValid(func):
    def inner(request,*args,**kwargs):
        ##校验登录
        cookie_email = request.COOKIES.get("buy_email")
        session_email = request.session.get("buy_email")
        if cookie_email and session_email and cookie_email == session_email:
            flag = LoginUser.objects.filter(email=cookie_email,id=request.COOKIES.get("buy_userid"),user_type=1).exists()
            if flag:
                return func(request,*args,**kwargs)
            else:
                return HttpResponseRedirect("/login/")
        else:
            return HttpResponseRedirect("/login/")
    return inner


## 首页
# @loginValid
def index(request):
    return render(request,"buyer/index.html")
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        if username and password:
            user = LoginUser.objects.filter(username=username,password=setPassword(password),user_type=1).first()
            if user:
                ## 成功登录
                response = HttpResponseRedirect("/")
                response.set_cookie("buy_email",user.email)
                response.set_cookie("buy_username",user.username)
                response.set_cookie("buy_userid",user.id)
                request.session["buy_email"] = user.email
                return response
            else:
                message = "账号密码不正确"
        else:
            message = "参数为空"

    return render(request,"buyer/login.html",locals())
def register(request):
    ## 接收参数
    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("pwd")
        repassword = request.POST.get("cpwd")
        email = request.POST.get("email")
        ## 校验数据
        if email and password and password == repassword:
            ## 有数据
            LoginUser.objects.create(email=email,password=setPassword(password),username=username)
            return HttpResponseRedirect("/login/")
        else:
            ## 参数为空
            message = "参数为空"

    return render(request,"buyer/register.html")

def logout(request):
    resp =  HttpResponseRedirect("/login/")
    resp.delete_cookie("buy_email")
    resp.delete_cookie("buy_username")
    resp.delete_cookie("buy_userid")
    del request.session["buy_email"]
    return resp





from django.shortcuts import render,render_to_response
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import *
from django.core.paginator import Paginator

# Create your views here.

import hashlib

## 登录装饰器
def loginValid(func):
    def inner(request,*args,**kwargs):
        ## 校验用户的身份
        cookie_username = request.COOKIES.get("username")
        session_username = request.session.get("username")
        if cookie_username and session_username and cookie_username == session_username:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/login/")
    return inner






## 密码 加密  md5
def setPassword(password):
    ### 需要实例化  md5 对象
    md5 = hashlib.md5()
    ## 对password 进行加密  参数为 bytes 类型
    md5.update(password.encode())
    result = md5.hexdigest()  ## 得到一个 16进制的加密结果
    return result

@loginValid
def index(request):
    ## 返回数据
    ## 1、 返回6条文章数据   排序  按照时间逆序


    article = Article.objects.order_by("-date")[:6]

    ## 2、 返回图文推荐文章内容  7条 图文推荐： 获取到推荐的文章   数据库中应该有推荐的字段 标识
    recommend_article = Article.objects.filter(recommend=1).order_by("-date")[:7]
    ## 3、 点击排行12条内容 有点击率 按照点击率进行逆序
    click_article = Article.objects.order_by("-click")[:12]
    return render_to_response("index.html",locals())


@loginValid
def about(request):
    return render_to_response("about.html")

def listpic(request):
    return render_to_response("listpic.html")


def newslistpic(request,page):
    ## 查询文章
    # article = Article.objects.all().order_by("id")    ## query set
    ## 根据类型对数据进行查询
    ## 获取类型
    article_type= request.GET.get("type")
    print(article_type)
    ## 根据类型查询到该类型下的文章
    A_type = Type.objects.filter(name=article_type).first()
    article = A_type.article_set.all()
    print(article)
    ## 将文章返回


    pagnitor_obj = Paginator(article,6)
    page_obj = pagnitor_obj.page(page)
    page_num = page_obj.number
    start = page_num - 2
    if start <= 2:
        start = 1
        end = start + 5
    else:
        end = page_num + 3
        if end >= pagnitor_obj.num_pages:
            end = pagnitor_obj.num_pages + 1
            start = end - 5
    page_range = range(start,end)
    return render_to_response("newslistpic.html",locals())
## 文章详情
def articleinfo(request,id):
    ## 查询指定文章的详情
    ## 文章的标识   id ‘
    article = Article.objects.get(id = id)
    ## 点击率 + 1
    article.click += 1
    article.save()

    return render_to_response("articleinfo.html",locals())

from .forms import UserForm
def register(request):
    ## 处理了 get请求，返回了注册页面
    ## 接收到用户的注册请求   post请求
    ## 将用户的数据   保存到数据库中
    ## 判断请求的方式
    userform = UserForm()
    if request.method == "POST":
        # data = request.POST
        # print(data)
        # username = request.POST.get("username")
        # password = request.POST.get("passwd")
        data = UserForm(request.POST)
        if data.is_valid():
            ## 进行校验，成功之后 返回 True  失败返回 Flase
            ##  获取到校验成功的数据
            print(data.cleaned_data)
            username = data.cleaned_data.get("username")
            password = data.cleaned_data.get("password")
            flag = User.objects.filter(username=username).exists()
            if flag:
                message = "用户已经存在"
            else:
                User.objects.create(username=username,password=setPassword(password))
                message = "注册成功"
        else:
            ## 校验失败
            message = data.errors
    return render(request,"register.html",locals())

## 返回  ajax 注册的页面
def ajax_register(request):
    ## 写处理业务的代码
    ## 代码  得到 数据
    return render(request,"ajax_register.html",locals())

## 处理ajax get请求
def ajax_get_req(request):
    """
    处理ajax 的get请求
        获取到ajax的值，进行查询数据库库，判断用户是否存在
    :param request:
        username  用户的账号
    :return:
        返回是否存在的结果
    """
    username = request.GET.get("username")
    print(username)
    result = {"code":10000,"msg":""}
    if username:
        flag = User.objects.filter(username = username).exists()
        if flag:
            ## True  账号存在
            result = {"code": 10001, "msg": "账号存在，请换一个"}
        else:
            ## flase  账号不存在
            # message = "账号不存在"
            result = {"code": 10000, "msg": "账号不存在,可用"}
    else:
        # message = "账号不能为空"
        result = {"code": 10002, "msg": "账号不能为空"}
    # return HttpResponse(message)
    return JsonResponse(result)

def ajax_post_req(request):
    """
    完成注册的需求
    :param request:
        username
        password
            将数据写入数据库中
    :return:
        Json对象  成功或者失败
    """

    result = {"code":10000,"msg":""}
    username = request.POST.get("username")
    password = request.POST.get("password")
    # print(request.POST)
    if username and password:
        ## 保存数据
        try:
            User.objects.create(username=username,password=setPassword(password))
            result = {"code": 10000, "msg": "注册成功"}
        except:
            result = {"code":10002,"msg":"注册失败"}
    else:
        result = {"code": 10001, "msg": "请求参数为空"}
    return JsonResponse(result)

def login(request):
    ## 判断登录
    if request.method == "POST":
        ## 获取值
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            ## 校验账号密码是否正确
            # flag = User.objects.filter(username=username,password=setPassword(password)).exists()
            user = User.objects.filter(username=username,password=setPassword(password)).first()
            if user:
                ## True
                # return HttpResponse("登录成功")
                # response = HttpResponse("登录成功")
                ## 参数：  要跳转的路径
                # response = HttpResponseRedirect("/article/index/")
                response = HttpResponseRedirect("/")
                ## 重定向到  首页
                ## 下发cookie 和session
                response.set_cookie("username",user.username)
                response.set_cookie("user_id",user.id)
                request.session["username"] = user.username
                return response
            else:
                return HttpResponse("账号密码不正确")
        else:
            ## 参数为空
            return HttpResponse("账号密码 不能为空")
    return render(request,"login.html")

## 退出
def logout(request):
    ## 删除cookie 和session
    ## 重定向到登录页
    response = HttpResponseRedirect("/login/")
    response.delete_cookie("username")
    del request.session["username"]

    return response








def search_artilce(request):
    search_key = request.GET.get("search_key")
    page = request.GET.get("page",1)
    if search_key:
        article = Article.objects.filter(title__contains=search_key).all()

        pagnitor_obj = Paginator(article, 10)
        page_obj = pagnitor_obj.page(page)
        page_num = page_obj.number
        start = page_num - 2
        if start <= 2:
            start = 1
            end = start + 5
        else:
            end = page_num + 3
            if end >= pagnitor_obj.num_pages:
                end = pagnitor_obj.num_pages + 1
                start = end - 5
        page_range = range(start, end)

    return render(request,"newslistpic.html",locals())


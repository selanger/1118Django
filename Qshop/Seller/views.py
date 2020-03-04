from django.shortcuts import render
from .models import LoginUser, Goods,GoodsType,ValidCode
import hashlib
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.paginator import Paginator


# Create your views here.
## 密码加密
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()

    return result


## 登录装饰器
def loginValid(func):
    def inner(request, *args, **kwargs):
        ##校验登录
        cookie_email = request.COOKIES.get("email")
        session_email = request.session.get("email")
        if cookie_email and session_email and cookie_email == session_email:
            flag = LoginUser.objects.filter(email=cookie_email, id=request.COOKIES.get("userid"), user_type=0).exists()
            if flag:
                return func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect("/seller/login/")
        else:
            return HttpResponseRedirect("/seller/login/")

    return inner


## 注册
def register(request):
    ## 接收参数
    if request.method == "POST":
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        email = request.POST.get("email")
        ## 校验数据
        if email and password and password == repassword:
            ## 有数据
            LoginUser.objects.create(email=email, password=setPassword(password), user_type=0)
            return HttpResponseRedirect("/seller/login/")
        else:
            ## 参数为空
            message = "参数为空"

    return render(request, "seller/register.html", locals())


## 登录
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            user = LoginUser.objects.filter(email=email, password=setPassword(password), user_type=0).first()
            if user:
                ## 成功登录
                response = HttpResponseRedirect("/seller/index/")
                response.set_cookie("email", user.email)
                response.set_cookie("userid", user.id)
                request.session["email"] = user.email
                return response
            else:
                message = "账号密码不正确"
        else:
            message = "参数为空"

    return render(request, "seller/login.html", locals())


## 首页
@loginValid
def index(request):
    return render(request, "seller/index.html")


##   退出
def logout(request):
    ## 删除 cookie session
    response = HttpResponseRedirect("/seller/login/")
    response.delete_cookie("email")
    del request.session["email"]
    return response


## 商品列表页面
@loginValid
def goods_list(request, status, page=1):
    ## 根据状态  查询商品
    ## status 状态的标识
    #  0  获取下架商品的数据
    # 1  获取在售商品的数据

    # goods = Goods.objects.all()
    # goods = Goods.objects.filter(goods_status=status).order_by("id")
    goods = Goods.objects.filter(goods_status=status,goods_store_id=request.COOKIES.get("userid")).order_by("id")
    goods_obj = Paginator(goods, 8)
    goods_list = goods_obj.page(page)

    # return render(request,"goods_list.html",locals())
    return render(request, "seller/goods_list.html",locals())


## 修改商品的状态
def goods_status(request, id, status):
    """
    修改商品的状态
    :param request:
    :param id:   商品的id
    :param status:
            up     上架
            down   下架
    :return:
    """
    goods = Goods.objects.get(id=id)
    if status == "up":
        ## 商品要上架
        goods.goods_status = 1
        goods.save()
    else:
        ## 代表商品要下架
        goods.goods_status = 0
        goods.save()
    url = request.META.get("HTTP_REFERER")  ## 得到请求的地址
    print(url)
    # return HttpResponseRedirect("/loginuser/goods_list/1/1/")
    return HttpResponseRedirect(url)


## 个人中心
@loginValid
def user_profile(request):
    ## 返回用户的信息
    ## 从session 或者 cokkie 这种获取登录的用户
    userid = request.COOKIES.get("userid")
    user = LoginUser.objects.get(id=userid)
    ## 处理post请求
    if request.method == "POST":
        data = request.POST
        print(data)
        user.email = data.get("email")
        user.phone_number = data.get("phone_number")
        user.username = data.get("username")
        user.age = data.get("age")
        user.gender = int(data.get("gender"))
        user.address = data.get("address")
        if request.FILES.get("img"):
            user.photo = request.FILES.get("img")
        user.save()
    return render(request, "seller/user_profile.html", locals())

##录入商品
@loginValid
def goods_add(request):
    goods_type = GoodsType.objects.all()
    if request.method == "POST":
        user_id = request.COOKIES.get("userid")
        data = request.POST
        goods = Goods()
        goods.goods_number = data.get("goods_number")
        goods.goods_name = data.get("goods_name")
        goods.goods_price = data.get("goods_price")
        goods.goods_count = data.get("goods_count")
        goods.goods_location = data.get("goods_location")
        goods.goods_safe_date = data.get("goods_safe_date")
        # goods.goods_picture = data.get("goods_number")
        goods.goods_type_id = int(data.get("goods_type"))
        goods.goods_store = LoginUser.objects.get(id=user_id)
        goods.goods_picture = request.FILES.get("img")
        goods.save()

    return render(request,'seller/goods_add.html',locals())

from sdk.sendDD import senddingding
import random
def get_code(request):
    result = {"code":10000,"msg":"验证码已发送"}
    ## 发送验证码
    ## 保存到数据库中
    email =request.GET.get("email")
    code = random.randint(1000,9999)
    params = {
        "content": "您的验证码为：{}，打死不要告诉别人！！！".format(code),
        "atMobiles": [],
        "isAtAll": True
    }
    try:
        ## 发送  使用钉钉
        senddingding(params)
        # 保存
        ValidCode.objects.create(email=email,code=code)
        result = {"code": 10000, "msg": "验证码已发送"}
    except:
        result = {"code": 10001, "msg": "验证码发送失败"}


    return JsonResponse(result)



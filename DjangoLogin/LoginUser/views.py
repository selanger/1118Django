from django.shortcuts import render
from .models import LoginUser,Goods
import hashlib
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse

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
        cookie_email = request.COOKIES.get("email")
        session_email = request.session.get("email")
        if cookie_email and session_email and cookie_email == session_email:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/login/")
    return inner




def register(request):
    ## 接收参数
    password = request.POST.get("password")
    repassword = request.POST.get("repassword")
    email = request.POST.get("email")
    ## 校验数据
    if email and password and password == repassword:
        ## 有数据
        LoginUser.objects.create(email=email,password=setPassword(password))
        return HttpResponseRedirect("/login/")
    else:
        ## 参数为空
        message = "参数为空"

    return render(request,"register.html",locals())

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            user = LoginUser.objects.filter(email=email,password=setPassword(password)).first()
            if user:
                ## 成功登录
                response = HttpResponseRedirect("/")
                response.set_cookie("email",user.email)
                request.session["email"] = user.email
                return response
            else:
                message = "账号密码不正确"
        else:
            message = "参数为空"

    return render(request,"login.html",locals())
@loginValid
def index(request):
    return render(request,"index.html")


def base(request):
    return render(request,"base.html")

##   退出
def logout(request):
    ## 删除 cookie session
    response = HttpResponseRedirect("/login/")
    response.delete_cookie("email")
    del request.session["email"]
    return response

## 商品列表页面
from django.core.paginator import Paginator
@loginValid
def goods_list(request,status,page=1):
    ## 根据状态  查询商品
    ## status 状态的标识
    #  0  获取下架商品的数据
    # 1  获取在售商品的数据

    # goods = Goods.objects.all()
    goods = Goods.objects.filter(goods_status=status).order_by("id")
    goods_obj = Paginator(goods,8)
    goods_list = goods_obj.page(page)

    return render(request,"goods_list.html",locals())

## 修改商品的状态
def goods_status(request,id,status):
    """
    修改商品的状态
    :param request:
    :param id:   商品的id
    :param status:
            up     上架
            down   下架
    :return:
    """
    goods = Goods.objects.get(id = id)
    if status == "up":
        ## 商品要上架
        goods.goods_status= 1
        goods.save()
    else:
        ## 代表商品要下架
        goods.goods_status = 0
        goods.save()
    url = request.META.get("HTTP_REFERER")   ## 得到请求的地址
    print(url)
    # return HttpResponseRedirect("/loginuser/goods_list/1/1/")
    return HttpResponseRedirect(url)


def goods_list_api(request,status,page=1):

    goods = Goods.objects.filter(goods_status=status).order_by("id")
    goods_obj = Paginator(goods,8)
    goods_list = goods_obj.page(page)
    ## json
    result = {"code":10000,"msg":"成功","data":""}
    res = []
    for one in goods_list:
        res_dict = {
            "id":one.id,
            "goods_number":one.goods_number,
            "goods_name":one.goods_name,
            "goods_price":one.goods_price,
            "goods_count":one.goods_count,
            "goods_location":one.goods_location,
            "goods_safe_date":one.goods_safe_date,
            "goods_status":one.goods_status,
        }
        res.append(res_dict)
    result["data"] = res
    result["page"]=page
    result["page_range"] = list(goods_obj.page_range)
    # return JsonResponse(result)
    ## 解决跨域请求
    response = JsonResponse(result)
    response["Access-Control-Allow-Origin"] = "*"    ## 添加允许访问的主机  域名
    return response



def goods_list_ajax(request):
    return render(request,'ajax_goods_list.html')








#
# import random
# ## 添加 100 商品
# def add_goods(request):
#     ## 循环
#     goods_name = "萝卜、马铃薯、藕、甘薯、山药、芋头、茭白、苤蓝、慈姑、洋葱、生姜、大蒜、蒜薹、韭菜花、大葱、韭黄、冬瓜、南瓜、西葫芦、丝瓜、黄瓜、茄子、西红柿、苦瓜、辣椒、玉米、小瓜、菠菜、油菜、卷心菜、苋菜、韭菜、蒿菜、香菜、芥菜、芥兰"
#     goods_name = goods_name.split("、")
#     goods_address = "石家庄、沈阳、哈尔滨、杭州、福州、济南、广州、武汉、成都、昆明、兰州、台北、南宁、银川、太原、长春、南京、合肥、南昌、郑州、长沙、海口、贵阳、西安、西宁、呼和浩特、拉萨、乌鲁木齐"
#     goods_address = goods_address.split("、")
#     for i,j in enumerate(range(100),1):
#         goods = Goods()
#         # goods_number 为  00001    00002   00100
#         goods.goods_number = str(i).zfill(5)
#         goods.goods_name = random.choice(goods_address)+random.choice(goods_name)
#         goods.goods_price = round(random.random()*100,2)  ## 保留小数点 2位
#         goods.goods_count = random.randint(1,100)    ##
#         goods.goods_location = random.choice(goods_address)
#         goods.goods_safe_date = random.randint(1,32)
#         goods.save()
#     return HttpResponse("add goods")
#
#


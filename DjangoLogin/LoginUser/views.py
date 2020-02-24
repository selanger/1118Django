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

    # return render(request,"goods_list.html",locals())
    return render(request,"goods_list_vue.html")

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



def vue_demo(request):
    name = "lisi"
    return render(request,"vue_demo.html",locals())





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

from django.views import View
## 类视图
class GoodsView(View):

    def __init__(self):
        super(GoodsView, self).__init__()
        # 统一返回结构
        self.result= {
            "version":"v1",
            "methods":"",
            "data":"",
            "msg":"",
            "code":""
        }
        self.obj = Goods

    ## 处理get请求
    def get(self,request):
        # result = {"methods":"get请求"}
        ## 获取id
        id = request.GET.get("id")
        if id:
            ## id存在的情况  返回这个id 对应的数据
            goods = self.obj.objects.filter(id=id).first()
            # print(goods)
            # result["data"] = goods  将对象直接返回，报错，因为不能够被json序列化
            data = {
                "goods_number":goods.goods_number,
                "goods_name":goods.goods_name,
                "goods_price":goods.goods_price,
                "goods_count":goods.goods_count,
                "goods_location":goods.goods_location,
                "goods_safe_date":goods.goods_safe_date,
                "goods_status":goods.goods_status,
            }
            # result["data"] = data
        else:
            ## id 不存在，返回所有的商品信息
            goods = self.obj.objects.all()
            data = []
            for one in goods:
                res = {
                    "goods_number": one.goods_number,
                    "goods_name": one.goods_name,
                    "goods_price": one.goods_price,
                    "goods_count": one.goods_count,
                    "goods_location": one.goods_location,
                    "goods_safe_date": one.goods_safe_date,
                    "goods_status": one.goods_status,
                }
                data.append(res)
            # result["data"] = data
        self.result["methods"] = "get请求"
        self.result["data"]= data
        self.result["code"] = 10000
        self.result["msg"] = "请求成功"
        return JsonResponse(self.result)
    ## 处理post请求
    def post(self,request):
        # 提交数据，保存数据
        data = request.POST
        goods = Goods()
        goods.goods_number = data.get("goods_number")
        goods.goods_name = data.get("goods_name")
        goods.goods_price = data.get("goods_price")
        goods.goods_count = data.get("goods_count")
        goods.goods_location = data.get("goods_location")
        goods.goods_safe_date = data.get("goods_safe_date")
        goods.save()

        self.result["methods"] = "post请求"
        self.result["data"]= {"id":goods.id}
        self.result["code"] = 10000
        self.result["msg"] = "保存数据成功"
        return JsonResponse(self.result)
    ## 处理put请求
    def put(self,request):

        ## 获取id
        ##  put 请求参数如何获取，不在GET中，也不在post而是在body中
        import json
        # data = request.body    ## b''   b'{"id":1}'   bytes
        # ## 将bytes 类型 转化为 string
        # data = data.decode()
        # print(data)
        # data = json.loads(data)
        # print(data)
        # id = data.get("id")
        # print(id)
        data = json.loads(request.body.decode())
        ## 需求： 通过id 修改某个商品的名字
        id = data.get("id")
        goods_name = data.get("goods_name")
        # 判断
        flag = Goods.objects.filter(id=id).exists()
        if flag:
            ## 存在
            ## 修改
            Goods.objects.filter(id=id).update(goods_name=goods_name)

            self.result["methods"] = "put请求"
            self.result["data"]= {"id":id}
            self.result["code"] = 10000
            self.result["msg"] = "修改数据成功"
        else:
            ## 不存在
            self.result["methods"] = "put请求"
            self.result["data"]= {"id":id}
            self.result["code"] = 10001
            self.result["msg"] = "商品不存在"

        return JsonResponse(self.result)

    ## 处理delete 请求你
    def delete(self,request):
        ## delete请求的参数  在 body中
        import json
        data = json.loads(request.body.decode())
        id = data.get("id")
        ## 删除操作
        Goods.objects.filter(id = id).delete()
        self.result["methods"] = "delete请求"
        self.result["data"] = {"id": id}
        self.result["code"] = 10000
        self.result["msg"] = "商品删除成功"
        return JsonResponse(self.result)

from django.middleware.csrf import get_token
## 获取csrftokoen
def gettoken(request):
    token = get_token(request)
    return JsonResponse({"token":token})


from .serializers import GoodsSerializers
from rest_framework import mixins,viewsets

class GoodsViews(mixins.CreateModelMixin,     ## 创建
                 mixins.UpdateModelMixin,     ## 更新
                 mixins.DestroyModelMixin,    ## 删除
                 mixins.ListModelMixin,       ###列表
                 mixins.RetrieveModelMixin,   ## 检索
                 viewsets.GenericViewSet):    ## rest的基类
    queryset = Goods.objects.all()     ## 返回的数据
    serializer_class = GoodsSerializers

from .serializers import UserSerializers
class UserViews(mixins.CreateModelMixin,     ## 创建
                 mixins.UpdateModelMixin,     ## 更新
                 mixins.DestroyModelMixin,    ## 删除
                 mixins.ListModelMixin,       ###列表
                 mixins.RetrieveModelMixin,   ## 检索
                 viewsets.GenericViewSet):    ## rest的基类
    queryset = LoginUser.objects.all()     ## 返回的数据
    serializer_class = UserSerializers






from django.shortcuts import render
import hashlib
from django.http import HttpResponseRedirect
from Seller.models import LoginUser,GoodsType,Goods
from .models import PayOrder,OrderInfo


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
    """
    1、如果类型下面没有商品，类型不展示
    2、如果类型下面超过4个商品，应该展示4个
    3、如果类型下面商品 大于0 小于 4  应该展示商品
    """
    goods_type = GoodsType.objects.all()
    ## 处理返回的数据  构建数据
    ## res = [{"type":"新鲜水果.obj","goods":[goods1,goods2,goods3,goods4]},{},{}]
    res = []
    for one in goods_type:
        goods = one.goods_set.order_by("id").all()
        if len(goods) > 4:
            goods_list = goods[:4]
            res.append({"type":one,"goods_list":goods_list})
        elif len(goods) > 0 and len(goods) <= 4:
            goods_list = goods
            res.append({"type": one, "goods_list": goods_list})

    return render(request,"buyer/index.html",locals())
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


def base(request):
    return render(request,"buyer/base.html")

## 商品列表页面
def goods_list(request):
    kywards = request.GET.get("kywards")
    req_type = request.GET.get("req_type")
    ## 判断请求的方式
    if req_type == "find_all":
        ## 查看更多
            ## kywards 应该为 类型的id
        goods_type = GoodsType.objects.filter(id = int(kywards)).first()
        goods = goods_type.goods_set.order_by("-goods_pro_time")

    else:
        ## 搜索
            ## kywards 应该为 商品的名字
            ## 模糊查询
        goods = Goods.objects.filter(goods_name__contains= kywards).order_by("-goods_pro_time")
    goods_new = goods[:2]
    return render(request,"buyer/goods_list.html",locals())




## 商品详情页
def goods_detail(request):
    ##  通过商品的id 获取商品
    goods_id = request.GET.get("goods_id")
    goods = Goods.objects.get(id= int(goods_id))
    return render(request,"buyer/goods_detail.html",locals())

def get_order_no():
    import uuid
    order_no = str(uuid.uuid4())
    return order_no
## 订单页面
@loginValid
def place_order(request):
    ## 保存数据
    ## 获取 买家的user_id
    user_id = request.COOKIES.get("buy_userid")
    goods_id = request.GET.get("goods_id")
    goods_count = int(request.GET.get("goods_count"))
    ## 查找商品
    goods = Goods.objects.get(id=goods_id)
    ##payorder
    payorder = PayOrder()
    payorder.order_number = get_order_no()
    payorder.order_status = 1   ### 未支付状态
    payorder.order_total = goods_count * goods.goods_price
    payorder.order_user_id = int(user_id)
    payorder.save()


    order_info = OrderInfo()
    order_info.order = payorder
    order_info.goods = goods
    order_info.goods_price = goods.goods_price
    ## 店铺的信息 通过商品寻找 店铺
    order_info.store = goods.goods_store
    order_info.goods_count = goods_count
    order_info.goods_total_price = goods_count * goods.goods_price
    order_info.save()

    ## orderinfo
    return render(request,"buyer/place_order.html",locals())










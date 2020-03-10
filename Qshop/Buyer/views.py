from django.shortcuts import render
import hashlib
from django.http import HttpResponseRedirect,JsonResponse
from Seller.models import LoginUser,GoodsType,Goods
from .models import PayOrder,OrderInfo,Cart,UserAddress,PayorderAddress



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
    order_no = str(uuid.uuid4()).replace("-","")
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
    user_address = UserAddress.objects.filter(user_id=user_id,status=1).first()

    ## orderinfo
    return render(request,"buyer/place_order.html",locals())


## 聚合函数
from django.db.models import Sum,Count,F,Q
def goods_test(request):
    order_id = 21
    pay_order = PayOrder.objects.get(id = order_id)
    ## 聚合方法   aggregate
    ## 返回值： 字典
    ## key 是默认的 goods_count__聚合方法
    ## 可以修改key
    sum_goods = pay_order.orderinfo_set.aggregate(Sum("goods_count"),
                                                  mycount = Count("id") )
    return render(request,"buyer/goods_test.html",locals())

from Qshop.settings import alipay
## 支付宝支付
@loginValid
def alipay_order(request):
    ## 获取订单  payorder _id
    payorder_id = request.GET.get("payorder_id")
    payorder = PayOrder.objects.get(id=payorder_id)
    ## 保存订单和地址的关系
    user_id = request.COOKIES.get("buy_userid")
    user_address = UserAddress.objects.filter(user_id=user_id,status=1).first()     ### 获取用户当前的地址
    ## 保存关系
    PayorderAddress.objects.create(name=user_address.name,
                                                      address= user_address.address,
                                                      phone=user_address.phone,
                                                      payorder=payorder)




    # 3、 实例化一个订单
    order_string = alipay.api_alipay_trade_page_pay(
        subject="生鲜交易",  ## 主题
        out_trade_no= payorder.order_number,  ## 订单号
        total_amount= str(payorder.order_total),  ## 交易金额   字符串
        return_url="http://127.0.0.1:8000/buyer/pay_result/",  ##  回调的地址
        notify_url=None  ## 通知
    )

    # 4、 返回支付宝支付的url
    result = "https://openapi.alipaydev.com/gateway.do?" + order_string
    return HttpResponseRedirect(result)

## 接收支付宝的支付结果
def pay_result(request):
    out_trade_no = request.GET.get("out_trade_no")
    ## 修改订单的状态  未付款 -》 已付款
    payorder = PayOrder.objects.get(order_number=out_trade_no)
    payorder.order_status = 2
    payorder.save()

    return render(request,"buyer/pay_result.html",locals())

from django.db.models import Sum
## 购物车
@loginValid
def cart(request):
    ## 查看 登录用户的购物车内容
    user_id = request.COOKIES.get("buy_userid")
    cart = Cart.objects.filter(cart_user=LoginUser.objects.get(id=int(user_id))).all()

    ## 获取购物车中所有商品的 小计之和 以及 商品的数量之和
    ## 聚合  all_total 字典  key：vlaue  ->  {"sum_total":3232,"sum_number":3232}
    all_total = cart.aggregate(sum_total = Sum("goods_total"),sum_number = Sum("goods_number"))

    return render(request,"buyer/cart.html",locals())

## 添加购物车
@loginValid
def add_cart(request):
    result = {"code":10000,"msg":"添加购物车成功"}
    data = request.POST
    ## 从cookie中获取买家
    user_id = request.COOKIES.get("buy_userid")
    print(data)
    goods_id = data.get("goods_id")
    goods_count = int(data.get("goods_count",1))  ## 商品详情页
    goods = Goods.objects.get(id = goods_id)

    ## 判断购物车中是否已经存在该商品
    cart = Cart.objects.filter(goods = goods).first()
    if cart:
        ## 存在
        cart.goods_number += goods_count
        # cart.goods_total = goods.goods_price * (goods_count + cart.goods_number)
        cart.goods_total += goods.goods_price * goods_count
    else:
        ## 不存在
        cart = Cart()
        cart.goods = goods
        cart.goods_number = goods_count
        cart.goods_total = goods_count * goods.goods_price
        cart.cart_user_id = user_id
    try:
        cart.save()
        result = {"code":10000,"msg":"添加购物车成功"}
    except:
        result = {"code": 10001, "msg": "添加购物车失败"}
    return JsonResponse(result)

def change_cart(request):
    result = {"code":10001,"msg":"计算失败","data":{}}
    ## 修改购物车的数量 以及小计
    ##   购物车id
    ## 操作的类型    add reduce

    data= request.POST
    print(data)
    cart_id = request.POST.get("cart_id")
    js_type = request.POST.get("js_type")
    if cart_id and js_type:
        cart = Cart.objects.filter(id = int(cart_id)).first()
        if cart:
            if js_type == "add":
                ## 加 操作
                cart.goods_number += 1
                cart.goods_total += cart.goods.goods_price
            else:
                ##减操作
                cart.goods_number -= 1
                cart.goods_total -= cart.goods.goods_price
            try:
                cart.save()
                result = {"code":10000,"msg":"操作成功","data":{"goods_number":cart.goods_number,"goods_total":cart.goods_total}}
            except:
                result = {"code":10003,"msg":"操作失败"}

        ## 将修改之后结果 返回到前端
        else:
            result = {"code": 10002, "msg": "商品不存在", "data": {}}

    return JsonResponse(result)




## 购物车 去结算
@loginValid
def cart_place_order(request):
    ## 获取购物车 id
    data = request.POST
    res = []   ### 购物车id
    for key,value in data.items():
        # print(key)
        # print(value)
        if key.startswith("cart_id"):
            res.append(value)
    print(res)
    ## 将购物中选中的商品 生成订单
    user_id = request.COOKIES.get("buy_userid")
    ## 查找商品
    ##payorder
    payorder = PayOrder()
    payorder.order_number = get_order_no()
    payorder.order_status = 1   ### 未支付状态
    payorder.order_total = 0   ## 订单总价  =  订单详情中的小计的和
    payorder.order_user_id = int(user_id)
    payorder.save()

    ### 生成订单详情
    for one in res:
        ## 查找购物车
        cart = Cart.objects.filter(id = one).first()
        order_info = OrderInfo()
        order_info.order = payorder
        order_info.goods = cart.goods
        order_info.goods_price = cart.goods.goods_price
        ## 店铺的信息 通过商品寻找 店铺
        order_info.store = cart.goods.goods_store
        order_info.goods_count = cart.goods_number
        order_info.goods_total_price = cart.goods_total
        order_info.save()
        cart.delete()

    payorder_total = payorder.orderinfo_set.aggregate(sum_total = Sum("goods_total_price")).get("sum_total")
    payorder.order_total = payorder_total
    payorder.save()

    return render(request,"buyer/place_order.html",locals())

## 我的订单
@loginValid
def user_center_order(request):
    ## 个人订单
    buy_userid = request.COOKIES.get("buy_userid")
    user = LoginUser.objects.filter(id = buy_userid).first()
    payorder_all = PayOrder.objects.filter(order_user =user).all()
    return render(request,"buyer/user_center_order.html",locals())
from django.core.cache import cache
from django.http import HttpResponse
def get_cachegoods(request):

    goods_id = request.GET.get("id")
    # goods = Goods.objects.filter(id = goods_id).first()
    # goods_name = goods.goods_name
    ## 从缓存中查询
    goods_cache = cache.get(goods_id)
    if goods_cache:
        print("11111111")
        goods_name = goods_cache
    else:
        print("2222222")
        goods = Goods.objects.filter(id = goods_id).first()
        goods_name = goods.goods_name
        ## 设置缓存
        cache.set(goods_id,goods_name,20)
    return HttpResponse(goods_name)


def update_cachegoods(request):
    goods_id = request.GET.get("id")
    goods_name = request.GET.get("goods_name")

    ##  删除缓存
    data = cache.get(goods_id)
    if data:
        cache.delete(goods_id)
    ## 更新数据
    Goods.objects.filter(id=goods_id).update(goods_name=goods_name)
    return HttpResponse("update cache goods")

## 个人中心
@loginValid
def user_center_info(request):
    buy_userid = request.COOKIES.get("buy_userid")
    user = LoginUser.objects.filter(id=buy_userid).first()
    return  render(request,"buyer/user_center_info.html",locals())


## 个人地址
@loginValid
def user_center_site(request):
    ## get请求   获取当前的地址
    buy_userid = request.COOKIES.get("buy_userid")
    user = LoginUser.objects.filter(id=buy_userid).first()
    # useraddress = UserAddress.objects.filter(user=user).first()

    ## post请求   提交新的地址
    if request.method == "POST":
        print(request.POST)
        data = request.POST
        UserAddress.objects.create(name=data.get("name"),
                                   address=data.get("address"),
                                   phone=data.get("phone"),
                                   user=user
                                   )
    useraddress = UserAddress.objects.filter(user=user).all()
    return  render(request,"buyer/user_center_site.html",locals())


## 修改默认地址的视图
@loginValid
def update_useraddress(request):
    if request.method == "POST":
        data = request.POST
        address_id = request.POST.get("address")
        buy_userid = request.COOKIES.get("buy_userid")
        user = LoginUser.objects.filter(id=buy_userid).first()
        print(data)
        ## 修改用户地址的状态
        ## 将之前的地址状态  改为 0
        UserAddress.objects.filter(user=user).update(status=0)
        ## address_id 地址修改为当前使用的地址  改为1
        UserAddress.objects.filter(id=address_id).update(status=1)
    return HttpResponseRedirect("/buyer/user_center_site/")









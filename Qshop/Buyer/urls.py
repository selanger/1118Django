from django.urls import path,include
from .views import *

urlpatterns = [
    path("index/",index),
    path("login/",login),
    path("register/",register),
    path("logout/",logout),
    path("goods_list/",goods_list),
    path("goods_detail/",goods_detail),
    path("place_order/",place_order),
    path("alipay_order/",alipay_order),
    path("pay_result/",pay_result),
    path("cart/",cart),
    path("add_cart/",add_cart),
    path("change_cart/",change_cart),
    path("cart_place_order/",cart_place_order),
    path("user_center_order/",user_center_order),
    path("get_cachegoods/",get_cachegoods),
    path("update_cachegoods/",update_cachegoods),
    path("user_center_info/",user_center_info),
    path("user_center_site/",user_center_site),
    path("update_useraddress/",update_useraddress),
]

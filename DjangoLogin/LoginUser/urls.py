from django.urls import path,re_path
from LoginUser.views import *
from rest_framework.routers import SimpleRouter
router = SimpleRouter()    ### 实例化一个对象
## 将视图进行注册
router.register(r"API/Goods",GoodsViews)
router.register(r"API/Users",UserViews)



urlpatterns = [
    path("goods_list/",goods_list),
    path("goods_list_ajax/",goods_list_ajax),
    # re_path("goods_list/(?P<page>\d+)/",goods_list),
    re_path("goods_list/(?P<page>\d+)/(?P<status>\d+)/",goods_list),
    re_path("goods_list_api/(?P<page>\d+)/(?P<status>\d+)/",goods_list_api),
    re_path("goods_status/(?P<id>\d+)/(?P<status>\w+)/",goods_status),
    path("vue_demo/",vue_demo)
]

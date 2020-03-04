from django.urls import path,re_path
from .views import *

urlpatterns = [
    path("login/",login),
    path("register/",register),
    path("index/",index),
    path("logout/",logout),
    path("user_profile/",user_profile),
    path("goods_add/",goods_add),
    path("get_code/",get_code),
    re_path("goods_list/(?P<page>\d+)/(?P<status>\d+)/", goods_list),
    re_path("goods_status/(?P<id>\d+)/(?P<status>\w+)/", goods_status),
]

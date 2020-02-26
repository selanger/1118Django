from django.urls import path,include
from .views import *

urlpatterns = [
    path("index/",index),
    path("login/",login),
    path("register/",register),
    path("logout/",logout),
    path("goods_list/",goods_list),
    path("goods_detail/",goods_detail),
]

from django.urls import path,re_path
from .views import *
urlpatterns = [
    path("index/",index),
    path('about/',about,name="myabout"),
    path("listpic/",listpic),
    path("choices_test/",choices_test),
    # path("newslistpic/",newslistpic),
    re_path("newslistpic/(?P<page>\d+)/",newslistpic),
    re_path("fy_test/(?P<page>\d+)/",fy_test),
    # path("add_article/",add_article),
    # path("articleinfo/",articleinfo),
    re_path("articleinfo/(?P<id>\d*)/",articleinfo),
]

from django.urls import path,re_path
from .views import *
urlpatterns = [
    path("index/",index),
    path('about/',about,name="myabout"),
    path("listpic/",listpic),
    # path("newslistpic/",newslistpic),
    re_path("newslistpic/(?P<page>\d+)/",newslistpic),
    # path("add_article/",add_article),
    # path("articleinfo/",articleinfo),
    re_path("articleinfo/(?P<id>\d*)/",articleinfo),
    path("register/",register),
    path("ajax_register/",ajax_register),
    path("ajax_get_req/",ajax_get_req),
    path("ajax_post_req/",ajax_post_req),
    path("search_artilce/",search_artilce),
]

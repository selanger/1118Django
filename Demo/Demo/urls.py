"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from .views import *
# from app01 import views as app01_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('about/',about,name="myabout"),
    re_path("^$",index),
    re_path("retest/(\d)/",retest),
    # re_path("testdemo/(\d{4})/(\w*)/",testdemo),
    # re_path("testdemo/(?P<year>\d{4})/(?P<city>\w*)/",testdemo),
    re_path("test/(\d{4})/(?P<city>\w*)/",test),
    re_path("indexhtml/(\d*)/",indexhtml),
    path("getindex",getindex),
    path("temptest/",temptest),
    path("statictest/",statictest),
    path("listpic/",listpic),
    path("base/",base),
    path("demo01/",demo01),
    # path("app01_index",app01_views.index),
    path("app01/",include("app01.urls"))

]

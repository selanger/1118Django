from django.urls import path
from .views import *


urlpatterns = [
    path("adduser/",adduser),
    path("getuser/",getuser),
    path("update_user/",update_user),
    path("delete_user/",delete_user),
    path("double_line/",double_line),
]
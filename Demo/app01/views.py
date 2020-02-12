from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse("我是子应用app01中的index视图")
    return render(request,"index.html")

def about(request):
    return HttpResponse("我是app01 中的about")


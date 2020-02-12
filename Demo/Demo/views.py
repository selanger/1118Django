from django.http import HttpResponse
# def index(request):
#     """
#     视图：作用
#     :param request:  形参 包含请求信息的请求对象
#     :return:    HttpResponse  响应对象
#     """
#     ## JsonReponse
#     return HttpResponse("hello world")

# def about(request):
#     import time
#     now_time = time.localtime()
#     now_time = time.strftime("%Y-%m-%d %H:%M:%S",now_time)
#
#     return HttpResponse(now_time)

def retest(request,id):
    print(id)
    return HttpResponse("我是retest视图")

def testdemo(request,city,year1111111):
    result = "我%s年在%s" % (year1111111,city)
    return HttpResponse(result)

def test(request,id,city):
    ## id 和 no 属于位置参数  只是 占位
    result = "%s,%s" %(id,city)
    print(result)
    print("git hub 远程")
    return HttpResponse(result)

from django.template import Template,Context
def indexhtml(request,age):
    """
    编写一个html页面
    :param request:
    :return:
    """

    html = """
    <html>
        <head></head>
        <body>
            <h1>我是index页面</h1>
            <img src="https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1732950921,2736360437&fm=26&gp=0.jpg">
        </body>
        姓名：{{ name }}
        年龄：{{ age }}
    </html>
    """
    ## 返回一个响应对象
    # return HttpResponse(html)
    ## 渲染动态的数据
    # 1.创建模板
    template_ojb = Template(html)
    # 2.构建动态数据
    parmas = {"name":"古天乐","age":age}    #### 字典
    content_obj = Context(parmas)
    # 3. 构建动态页面 将动态数据 渲染到静态页面上
    result = template_ojb.render(content_obj)
    return HttpResponse(result)

##导包
from django.template.loader import get_template
def getindex1(request):
    ## 第一种方式
    ## 返回页面  返回 templates中的index.html 页面
    ## 创建一个模板对象
    template_obj = get_template("index.html")
    ## 创建一个返回对象
    ## 完成动态数据的渲染
    params = {"name":"zhangsan","age":19}
    result = template_obj.render(params)
    return HttpResponse(result)
## 导包
from django.shortcuts import render_to_response
def getindex1(request):
    ## 第二种方式
    ## 返回index 页面
    ## 返回动态的数据
    params = {"name":"lisi","age":20}
    # render_to_response(要返回的页面，)
    return render_to_response("index.html",params)

## 导包
from django.shortcuts import render
def getindex(request):
    ## 第三种
    ## 返回的是index.html
    ## 渲染的数据     name age
    ## render(request,要返回的页面,动态的数据)
    parmas = {"name":"wangwu","age":19}
    return render(request,"index.html",parmas)


def temptest(request):
    ## 返回数据
    name = "lao liu"
    user_name = "lisi"
    age = 20
    hobby = ["唱歌","跳舞","lol"]
    score = {"python":100,"java":90,"php":80}
    subject= {"python","java","php"}

    ## 返回数据的方式
    # 第一种
    # return render_to_response("temptest.html",{"name":user_name,"age":age,"hobby":hobby,"score":score,"subject":subject})
    # 第二种
    # parmas = {"name":"wangwu","age":19}
    # return render(request,"index.html",parmas)
    ## 第三种  locals()
    ## locals()  会将所有的局部变量作为字典返回
    ##
    import datetime
    now_time = datetime.datetime.now()
    import time

    myjs = """
    <script>
        alert("myjs");
    </script>
    """
    return render_to_response("temptest.html",locals())


def statictest(request):

    return render_to_response("statictest.html")



def index(request):

    return render_to_response("index.html")


def about(request):
    return render_to_response("about.html")

def listpic(request):
    return render_to_response("listpic.html")


def base(request):
    return render_to_response("base.html")

def demo01(request):
    return render_to_response("demo01.html")






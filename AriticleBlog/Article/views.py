from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    ## 返回数据
    ## 1、 返回6条文章数据   排序  按照时间逆序
    article = Article.objects.order_by("-date")[:6]
    ##
    # one = article[0]
    # print(one)
    # print(one.author)
    # print(one.type.first())



    ## 2、 返回图文推荐文章内容  7条
    ##  图文推荐： 获取到推荐的文章   数据库中应该有推荐的字段 标识
    recommend_article = Article.objects.filter(recommend=1).order_by("-date")[:7]



    ## 3、 点击排行12条内容
    ## 有点击率
    ##  按照点击率进行逆序
    click_article = Article.objects.order_by("-click")[:12]



    return render_to_response("index.html",locals())


def about(request):
    return render_to_response("about.html")

def listpic(request):
    return render_to_response("listpic.html")


def newslistpic(request,page):
    ## 查询文章
    article = Article.objects.all().order_by("id")    ## query set
    pagnitor_obj = Paginator(article,6)
    page_obj = pagnitor_obj.page(page)
    ## 通过遍历  pagnitor_obj.page_range -> range(1,11)
    ## 解决 页码数量多 方法  修改 pagnitor_obj.page_range  1  11

    ## 获取当前的页码     3 4 5 6 7 8      [2,7]
    ##       0 1 2 3 4 5
    ##  2      1 2 3 4 5
    ## 1      1 2 3 4 5
    ## 17      13 14 15 16 17
    page_num = page_obj.number
    ## start
    start = page_num - 2
    if start <= 2:
        start = 1
        end = start + 5
    ## end
    else:
        end = page_num + 3
        if end >= pagnitor_obj.num_pages:  ## 17 range(start,17)
            end = pagnitor_obj.num_pages + 1
            start = end - 5
    # page_range = pagnitor_obj.page_range[start:end]
    page_range = range(start,end)

    return render_to_response("newslistpic.html",locals())
## 文章详情
def articleinfo(request,id):
    ## 查询指定文章的详情
    ## 文章的标识   id ‘
    article = Article.objects.get(id = id)

    return render_to_response("articleinfo.html",locals())


def fy_test(request,page):
    print(page)


    ## 查询文章的方法
    article = Article.objects.all().order_by("id")
    # print(article)
    ## Paginator(数据集，每页展示的条数)
    paginator_obj = Paginator(article,10)
    print(paginator_obj)
    # print(paginator_obj.count)    ### 数据的总条数
    # print(paginator_obj.num_pages)   ###  总页数
    # print(paginator_obj.page_range)   ##  range(1, 4)

    page_obj = paginator_obj.page(page)
    # print(page_obj)   #   <Page 1 of 11>
    ## 循环遍历  得到分页之后的数据
    for one in page_obj:
        print(one)
    # print(page_obj.has_next())    ## 是否有下一页  True  False
    # print(page_obj.has_previous())    ## 是否有上一页  True  False
    # print(page_obj.number)    ## 返回当前所在的页码
    # print(page_obj.previous_page_number())   ## 上一页的页码
    # print(page_obj.next_page_number())     ## 下一页的页码
    # print(page_obj.has_other_pages())   ## 是否有其他的页

    return HttpResponse("fy test")




## 增加多条数据
def add_article(request):

    for i in range(100):
        article = Article()
        article.title = "title_%s" % i
        article.content = "content_%s" % i
        article.description = "description_%s" % i
        article.author = Author.objects.get(id =1)
        article.save()
        ## 多对多关系中   add
        article.type.add(Type.objects.get(id = 1))
        article.save()

    return HttpResponse("add article")







def choices_test(request):
    data = Author.objects.get(id =1)
    gender = data.gender
    print(gender)
    gender = data.get_gender_display()
    print(gender)


    return HttpResponse("choices_test")


def request_demo(request):
    ## 学习请求 提供的方法
    # print(dir(request))
    """
    ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding', '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_read_started', '_set_post', '_stream', '_upload_handlers', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_raw_uri', 'get_signed_cookie', 'headers', 'is_ajax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user', 'xreadlines']

    """
    # print(request.COOKIES)   ###  标识用户的身份
    # print(request.FILES)    ###  上传的文件例如： 图片，文档
    ## GET  get请求传递的参数
    # name = request.GET.get("name")
    # age = request.GET.get("age")
    # print(name)
    # print(age)
    # print(request.method)
    # print(request.scheme)
    # print(request.path)
    print(request.META)
    print(request.META.get("HTTP_REFERER"))
    # print(request.META.get("OS"))
    print(request.META.get("HTTP_HOST"))
    return HttpResponse("request demo")


def get_test(request):
    data = request.GET
    print(data)
    name = request.GET.get("name")
    age = request.GET.get("age")
    return HttpResponse("get_test，姓名为{}，年龄为{}".format(name,age))

def post_test(request):
    data = request.POST
    print(data)
    name = request.POST.get("name")
    age = request.POST.get("age")
    return HttpResponse("posttest 姓名{} 年龄{}".format(name,age))

def getdemo(request):
    # data = request.GET
    # print(data)
    # search = request.GET.get("search")
    # print(search)
    # data = request.GET.getlist("search")
    # print(data)

    ## 接收请求  处理请求   返回响应
    ## 获取到关键字
    search = request.GET.get("search")
    ## 查询数据库  得到文章的标题
    if search:
        ## 查询数据库
        article = Article.objects.filter(title__contains=search).values("title")
        if len(article) == 0:
            article = "没有对应的文章"
    ## 返回结果

    return render_to_response("getdemo.html",locals())

def qqtest(request):
    return  render_to_response("qqtest.html")


def postdemo(request):
    username = request.POST.get("username")
    password = request.POST.get("passwd")
    print(username)
    print(password)
    # return render_to_response("postdemo.html")
    return render(request,"postdemo.html")


def register(request):
    ## 处理了 get请求，返回了注册页面
    ## 接收到用户的注册请求   post请求
    ## 将用户的数据   保存到数据库中
    ## 判断请求的方式
    if request.method == "POST":
        data = request.POST
        print(data)
        username = request.POST.get("username")
        password = request.POST.get("passwd")
        ## 判断用户是否存在
        flag = User.objects.filter(username=username).exists()
        if flag:
            ## 存在
            ## 不注册
            message = "用户已经存在"
        else:
            ## 不存在
                ## 注册
            ## 保存数据
            User.objects.create(username=username,password=password)
            message = "注册成功"
    return render(request,"register.html",locals())


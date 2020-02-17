from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator

# Create your views here.


def index(request):

    return render_to_response("index.html")


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


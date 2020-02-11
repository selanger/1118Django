from django.http import HttpResponse
def index(request):
    """
    视图：作用
    :param request:  形参 包含请求信息的请求对象
    :return:    HttpResponse  响应对象
    """
    ## JsonReponse
    return HttpResponse("hello world")

def about(request):
    import time
    now_time = time.localtime()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S",now_time)

    return HttpResponse(now_time)

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





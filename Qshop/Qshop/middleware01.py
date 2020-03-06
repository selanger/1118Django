# 自定义  中间件
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.shortcuts import render

class MiddleWareTest(MiddlewareMixin):

    def process_request(self,request):
        """
          请求进来第一个被触发的方法
        :param request:  包含请求信息的请求对象
        :return:   当返回None 之后，才会执行下面的流程
        """
        print("process_request")
        ## 黑名单    不让某些ip 访问服务
        ip_list = ["10.10.10.10","198.1.1.1"]
        ## 获取访问的ip
        ip = request.META.get("REMOTE_ADDR")
        print(ip)
        if ip in ip_list:
            # return HttpResponse("请绕行，这里不适合你")
            return render(request,"seller/404.html")

    def process_view(self,request,callback,callbackargs,callbackkwargs):
        """
        请求经过 process_request 之后被触发的方法
        :param request:   request是包含请求信息的请求对象，但是有可能被process_request 处理
        :param callback:   处理请求的视图
        :param callbackargs:   参数    元祖
        :param callbackkwargs:    字典参数
            参数：  指通过 路由中的正则匹配到的内容
                元祖参数：   正则中使用组匹配
                字典参数：   正则中使用组匹配 + 别名
        :return:  None  执行下面的流程
        """
        print("process_view")
        print(callback)
        print(callbackargs)
        print(callbackkwargs)
        if callbackkwargs.get("version") == "v1":
            return HttpResponse("v1 版本太低")

    def process_exception(self,request,exception):
        """
         异常
        :param request:
        :param exception:
        :return:
        """
        print("process_exception")
        print(exception)
        ## 写 异常日志
        import os
        import time
        now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        from Qshop.settings import BASE_DIR
        file = os.path.join(BASE_DIR,"error.log")
        content = "[%s]:%s \n" % (now_time,str(exception))
        with open(file,"a") as f:
            f.write(content)
        return render(request,"seller/404.html")




    def process_template_response(self,request,response):
        """
        模板渲染  少见
        :param request:
        :param response:
        :return:
        """
        print("process_tempalte_resposne")
        return response
    def process_response(self,request,response):
        """
        返回响应   可以对所有的放回结果，做处理   例如：设置响应头  设置返回的数据类型，设置cookie session  版本号  统一返回的格式
        :param request:
        :param response:
        :return:
        """

        print("process_response")
        ## 设置cookie
        response.set_cookie("process_response","helloword")
        return response






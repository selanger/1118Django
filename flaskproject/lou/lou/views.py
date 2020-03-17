# 项目的 视图文件
from lou import app
from flask import render_template
from lou.models import *
from flask import request    ###  请求上下文

@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/courses/")
def courses():
    ## 获取 第几页  获取 每页多少条
    page = request.args.get("page",1)
    page = int(page)
    page_number = 12
    label_list = Label.query.all()
    label_id = request.args.get("label_id")    ## 标签id
    course_type = request.args.get("course_type")     ### 类别

    if label_id is None and course_type is None:
        ### 两者都不存在
        ## 返回所有的数据
        course_list = Course.query
    elif label_id is not None and course_type is None:
        ## 只有 label_id    通过标签获取课程
        # course_list = Label.query.filter(Label.id == label_id).first().course
        course_list = Course.query.filter(Course.lebal_id == label_id)
    elif label_id is None and course_type is not None:
        ## 只有course_type   通过类别获取课程
        course_list = Course.query.filter(Course.type == course_type)
    elif label_id and course_type:
        ## 两者都存在  通过类别和 标签获取数据
        course_list = Course.query.filter(Course.type==course_type,Course.lebal_id==label_id)

    data = request.args
    print(data)
    search = request.args.get("search")
    if search:
        course_list = Course.query.filter(Course.name.like("%{}%".format(search)))


    course_obj = course_list.paginate(page,page_number)
    course_list = course_obj.items

    ### 重写  range(start,end)
    ## 获取请求参数  构建结果 返回到前端页面
    data = request.args.to_dict()
    print(data)
    res_list = []
    for key,value in data.items():
        res = "%s=%s" % (key,value)
        res_list.append(res)

    params = "&".join(res_list)
    print(params)

    return render_template("courses.html",**locals())


@app.route("/fy/")
def fy():

    # course_obj = Course.query.filter(Course.name.like("%{}%".format("python"))).paginate(1,10)
    course_obj = Course.query.paginate(10,10)
    # paginate  属于flask sqlalchemy  中的方法
    ## 第一个参数  第几页
    ## 第二个参数  每页多少条
    print(course_obj)
    ## 分页之后的数据
    # data = course_obj.items
    # print(data)
    print(course_obj.has_prev)   ###   是否有上一页
    print(course_obj.prev_num)   ##  上一页的页码
    print(course_obj.has_next)   ###   是否有下一页
    print(course_obj.next_num)   ###   下一页的页码
    print(course_obj.page)   ###   当前页码
    print(course_obj.total)   ###   数据总条数
    print(course_obj.iter_pages)   ###   迭代器  range<1,3>  <---   page_range
    for one in course_obj.iter_pages():
        print(one)    ### 1 2 None 3 4 5 6 7 8 None 37 38

    return "分页"


#
# import random
# @app.route("/ac")
# def add_course():
#     result = [
#      {'src': 'https://dn-simplecloud.shiyanlou.com/ncn63.jpg', 'alt': '新手指南之玩转实验楼'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/ncn1.jpg', 'alt': 'Linux 基础入门（新版）'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/1480389303324.png', 'alt': 'Kali 渗透测试 - 后门技术实战（10个实验）'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/1480389165511.png', 'alt': 'Kali 渗透测试 - Web 应用攻击实战'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/1482113947345.png', 'alt': '使用OpenCV进行图片平滑处理打造模糊效果'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/1482807365470.png', 'alt': '使用 Python 解数学方程'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/1482215587606.png', 'alt': '跟我一起来玩转Makefile'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/1480386391850.png', 'alt': 'Kali 渗透测试 - 服务器攻击实战（20个实验）'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/1482113981000.png', 'alt': '手把手教你实现 Google 拓展插件'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/1482113522578.png', 'alt': 'DVWA之暴力破解攻击'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/1482113485097.png', 'alt': 'Python3实现简单的FTP认证服务器'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/1481689616072.png', 'alt': 'SQLAlchemy 基础教程'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/1481511769551.png', 'alt': '使用OpenCV&&C++进行模板匹配'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/1481512189119.png', 'alt': 'Metasploit实现木马生成、捆绑及免杀'},
#      {'src': 'https://dn-simplecloud.shiyanlou.com/1480644410422.png', 'alt': 'Python 3 实现 Markdown 解析器'}]
#     for i in range(25):
#         for cou in result:
#             c = Course()
#             name = cou.get("alt")
#             if i != 0:
#                 name +=" (%s)"%i
#             c.name = name  # 课程名称
#             c.description = "%s课程啊，真滴好啊"%name  # 课程描述
#             c.picture = cou.get("src")  # 课程logo
#             c.show_number = random.randint(1,100000)  # 观看人数
#             c.time_number = random.randint(7,32)  # 课时
#             c.label = random.choice(Label.query.all())
#             c.save()
#     return "hello world"


# @app.route("/addlabel/")
# def addlabel():
#     string = "Python C/C++ Linux Web 信息安全 PHP Java NodeJS Android GO Spark 计算机专业课 Hadoop HTML5 Scala Ruby R 网络 Git SQL NoSQL 算法 Docker Swift 汇编 Windows"
#     str_list = string.split(" ")
#     for one in str_list:
#         label = Label(name=one,description="%s课程" % one)
#         label.save()
#     return "添加标签"


@app.route("/v1/reqtest/",methods=["GET","POST","PUT","DELETE"])
def reqtest():
    # args
    # data = request.args   ### 类字典对象
    # print(data)
    # print(data.get("name"))
    # print(data.get("age"))
    # print(type(data.get("age")))    ### 字符串
    # print(data.to_dict())      ### 可以转换为字典
    # print(data.getlist("name"))
    ## 获取post请求传参
    # data = request.form
    # print(data.get("name"))
    # print(data.get("age"))
    # print(data.to_dict())
    # print(data.getlist("name"))
    # print(data)
    # print(request.method)
    # print(request.cookies)
    # print(request.referrer)
    # print(request.path)
    # print(request.host)   ## ip + port
    # print(request.host_url)   ## 协议 + ip + port
    print(request.files)
    img = request.files.get("xiaomeimei")
    # print(img.filename)
    print(img.filename)   ## 文件的名字 + 后缀
    print(img.content_type)   ## 文件的类型
    print(img.name)   ## 请求的 key
    img.save(img.filename)



    return "reqtest"



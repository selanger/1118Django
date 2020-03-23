from blueprintproject.course import course_bl
from blueprintproject.course.models import *
from flask_restful import Resource
from flask import render_template,request
from blueprintproject.user.views import LoginValid
from flask_restful import Resource

@course_bl.route("/index/")
def index():
    return render_template("index.html")



@course_bl.route("/courses/")
@LoginValid
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



class CoursesApi(Resource):

    def __init__(self):
        self.result = {
            "code":10000,
            "msg":"",
            "method":"",
            "data":{}
        }
    def get_data(self,data):
        resp_data = {
            "id": data.id,
            "name": data.name,
            "description": data.description,
            "picture": data.picture,
            "show_number": data.show_number,
            "status": data.status,
            "time_number": data.time_number,
        }
        return resp_data
    def get(self,id=None):
        self.result["method"] = "get请求"
        self.result["data"] = {"id":id}

        if id:
            ## id 存在的情况
            course = Course.query.get(id)   ### 对象
            resp_data = self.get_data(course)
        else:
            ## id 不存在
            ## 请求  参数 不固定     ?name=zzzz           ?name=sdfdsfds&status=1     ?status=1
            name = request.args.get("name")
            status = request.args.get("status")
            data = request.args     ### 获取到请求参数 -- 》 转字典   {"name":xxxx,"age":12}   ->   name=xxxxx,age=12
            data = data.to_dict()    ### 字典
            course = Course.query.filter_by(**data).all()
            resp_data = []
            for one in course:
                resp_obj = self.get_data(one)
                resp_data.append(resp_obj)
        self.result["data"] = resp_data
        return self.result

    def post(self):
        ###   保存数据
        data = request.form.to_dict()
        c = Course(**data,lebal_id=1)
        c.save()
        self.result["method"] = "post请求"
        self.result["data"] = {"id":c.id}
        return self.result
    def put(self):
        ## 更新数据
        id = request.form.get("id")
        if id:
            ## 更新数据
            c =  Course.query.get(id)    ### 对象
            ## 修改操作  对象的属性 重新赋值
            data = request.form.to_dict()  ### 字典  {"name":xxxx,"age":12}
            for key,value in data.items():
                ### 循环得到传值中的 key value
                ## 增加判断   id  不允许修改
                if key == "id":
                    pass
                setattr(c,key,value)
            c.update()
            self.result["data"] = {"id":id}
            self.result["msg"] = "修改成功"

        else:
            self.result["method"] = "put请求"
            self.result["msg"] = "缺少参数"
        return self.result
    def delete(self):
        ## 删除
        id = request.form.get("id")
        c = Course.query.get(id)
        if c:
            c.delete()
        self.result["data"] = {"id":id}
        self.result["method"] = "delete请求"
        self.result["msg"] = "删除成功"
        return self.result







# 导入模块
from flask import Flask
# 实例化一个  flask 应用app
app = Flask(__name__)


@app.route("/")     ### 路由
def index():       ### 视图
    return "hello world"    ## 返回值
@app.route("/hello/")
def hello1():
    return "你好1"
@app.route("/hello/")
def hello():
    return "你好"



@app.route('/test/<name>/<age>/')
def test(name,age):
    print(name)
    return "姓名：%s,年龄：%s" %(name,age)

@app.route("/mystring/<string:name>/")
def mystring(name):
    print(type(name))
    return "%s" %(name)

@app.route("/myint/<int:data>/")
def myint(data):
    print(type(data))
    return "%s" %(data)

@app.route("/myfloat/<string:data>/")
def myfloat(data):
    print(type(data))
    return "%s" %(data)

@app.route("/myuuid/<uuid:data>/")
def myuuid(data):
    print(type(data))
    return "%s" % data

@app.route("/mypath/<path:data>/")
def mypath(data):
    print(type(data))
    return "%s" % data

class Person:
    name="张三"
    age = 19


from flask import render_template
@app.route('/gethtml/')
def gethtml():
    # name = "zhangsan"
    # return render_template("demo.html",name="zhangsan",age=28,subject=["python","php","java"])

    name = "zhangsan"
    age = 28
    subject = ["python", "php", "java"]
    score = {"yuwen":100,"shuxue":89,"yingyu":90}
    person = Person()
    print(person.name)
    myhtml = "<a href='https://baidu.com'>百度</a>"
    # return render_template("demo.html",name=name,age=age,subject=subject)
    # params = {
    #     name:name,
    #     age:age,
    #     subject:subject
    # }
    # return render_template("demo.html",params=params)
    return render_template("demo.html",**locals())   ## **locals解包

## Django
## return render(request,"页面",{"name":"xxxx","age":23})
## return render(request,"页面",locals())   locals() 可以将局部变量作为字典返回

## 接收一个参数的过滤器
def myadd100(num1):
    num = num1 + 100
    return num
## 接收多个参数的过滤器
def myaddmany(num1,num2,num3,num4):
    return num1 + num2 + num3 + num4
app.add_template_filter(myadd100,"Myadd")
app.add_template_filter(myaddmany,"Myaddmany")



if __name__ == '__main__':
    app.run(host="127.0.0.1",port="8000",debug=True)   # 启动flask项目









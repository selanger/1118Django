from django.shortcuts import render
from django.http import HttpResponse
# 导入模型
from .models import User,Subject

# Create your views here.

def adduser(request):
    ## ORM操作
    ## 增加
    ## insert into user(id,user_name_age....) values(0,"sdfds",19...)
    ## save
    ## 第一种
    # user = User()
    # user.user_name = "lisi"
    # user.age = 18
    # user.phone = "15201010101"
    # user.email = "lisi@126.com"
    # user.save()
    ## 第二种
    # user = User(user_name="wangwu",age=20,phone="15201010102",email="wangwu@126.com")
    # user.save()

    ## create
    ## 1.能够增加数据
    ## 2.会将增加的当条数据 返回
    # User.objects.create(user_name="laoliu",age=21,phone="15201010103",email="laoliu@126.com")
    ## 第二种 字典
    params = dict(user_name = "laoqi", age = 22, phone = "15201010104", email = "laoqi@126.com")
    user = User.objects.create(**params)   ## 解包
    # User.objects.create({"user_name":"laoqi"})
    print(user)

    return HttpResponse("add user")


def getuser(request):
    ## 查询数据
    ## 1. all
    ##   返回符合条件的所有数据
    ## 结果： QuerySet
    ## select * from user;
    ## select user_name,age from user;
    # user = User.objects.all()
    #     # print (user)
    # print(user[0].user_name)
    # print(user[0].age)
    # # for one in user:
    #     print (one)
    #     print(one.user_name)

    # sub = Subject.objects.all()
    # print(sub)

    ## get方法
    ## 返回符合条件的数据
    ## 返回值类型  对象
    ## 如果没有数据  会报错  有多条数据 会报错
    ## get 方法返回符合条件的对象，返回值有且只有一条，在使用get方法的时候，通常条件为id

    # user = User.objects.get(id=2)
    # user = User.objects.get(user_name="zhangsan")
    # user = User.objects.get(age=20)
    # print(user)
    # print(user.user_name)


    ## filter   过滤筛选
    ## 返回符合条件的所有数据
    ## 返回值为 queryset
    ## select * from user where age = 20 and user_name="wangwu"
    # user = User.objects.filter(age=20,user_name="wangwu")
    # print(user)
    # print(user[0].user_name)

    ## exclude
    ## 返回不符合条件的数据
    # user = User.objects.exclude(age=20)
    # print(user)

    ## all 方法
    # user = User.objects.filter(age=20).all()
    # print (user)
    ## first
    ## first 返回符合条件的第一条数据   返回值为对象
    # user= User.objects.filter(age=20).first()
    # print(user)
    ## last
    ## 返回符合条件的最后一条数据 返回值为 对象
    # user = User.objects.filter(age =20).last()
    # print(user)

    # order_by  排序
    ## 升序
    # user = User.objects.filter(age=20).order_by("id","age").first()
    # print (user)
    # ## 降序
    # user = User.objects.filter(id=6).order_by("-id").first()
    # print (user)

    ## reverse 反转
    ## 返回结果   queryset
    ## reverse 使用条件，reverse 之前的结果必须是排序的，可以使用order_by 或者 ordering，先进行排序
    # user = User.objects.order_by("id").reverse()
    # print(user)
    # user = User.objects.order_by("id").all()
    # print(user)

    # values
    ## 返回的是queryset ，比较特殊，得到的是  [{},{}]
    ## select * from user;

    # user = User.objects.values()
    # print(user)
    # print(user[0]["user_name"])
    # ## select user_name,age from user;
    # user = User.objects.values("user_name","age")
    # print (user)
    # user = User.objects.filter(id=2).values("user_name","age")
    # print(user)


    ## count   计数
    ## 返回 数字
    # num = User.objects.filter(age=20).count()
    # print(num)
    # num = User.objects.count()
    # print (num)

    ##   exists 判断数据是否存在
    ## 返回值为  布尔值  True 和 False
    flag = User.objects.filter(age=20).exists()
    print(flag)


    ## 切片
    ##类似于  sql 中 limit
    user = User.objects.all()[0:2]
    print(user)

    return HttpResponse("get user")

def update_user(request):
    ## 更新数据
    ##save
    ## 查到 数据
    # user = User.objects.get(id=2)
    # user.user_name = "python"
    # user.save()

    # user = User.objects.filter(id=3).first()
    # user.user_name="java"
    # user.save()
    # user = User.objects.filter(age=20).all()  ## 结果  queryset
    # for one in user:
    #     one.user_name = "php"
    #     one.save()

    ## update
    data = User.objects.filter(age=22).update(user_name="python")
    print(data)
    # 报错
    # User.objects.get(id=2).update(user_name="java")
    return HttpResponse("update user")

def delete_user(request):
    ## 删除
    #  delete
    ## queryset.delete
    # User.objects.filter(id =2).delete()
    ## 删除 id = 4
    # object.delete
    # User.objects.get(id =4).delete()
    data = User.objects.filter(age=22).delete()
    print(data)


    return HttpResponse("delete user")


def double_line(request):
    ## 双下划线查询
    ## __lt   小于
    ##  查询  id 小于10 的数据
    # data = User.objects.filter(id__lt=10).all()
    # print(data)
    ## __gt   大于
    ## 查询 id 大于 10 的数据
    # data = User.objects.filter(id__gt =10).all()
    # print(data)
    ## __lte  小于等于
    # id 小于等于10 的数据
    # data = User.objects.filter(id__lte =10).all()
    # print(data)
    ## 报错  不能直接使用 大于 小于号
    # data = User.objects.filter(id < 10).all()
    # print(data)
    ## __gte  大于等于

    ## __in  范围查询
    ## 查询 id 为 8 9 10 99 100
    # data = User.objects.filter(id__in = [8,9,10,99,100]).all()
    # print(data)
    # data = User.objects.exclude(id__in = [8,9]).all()
    # print(data)

    ## __contains 模糊查询
    # data = User.objects.filter(user_name__contains="p").all()
    # print(data)
    # data = User.objects.filter(user_name__contains="lao").all()
    # print(data)
    # data = User.objects.filter(user_name__contains="ao").all()
    # print(data)
    ## __icontains 忽略大小写的模糊查询
    # data = User.objects.filter(user_name__icontains="lao").all()
    # print(data)

    ##  __startswith  开头
    data = User.objects.filter(user_name__startswith="lao").all()
    print (data)
    ## __istartswith 忽略大小写
    data = User.objects.filter(user_name__istartswith="lao").all()
    print (data)
    ## __endswith 判断结尾
    #  __iendswith 判断结尾 忽略大小写
    data = User.objects.filter(user_name__endswith='qi').all()
    print(data)


















    return HttpResponse("double line")











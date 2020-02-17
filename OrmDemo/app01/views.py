from django.shortcuts import render
from django.http import HttpResponse
# 导入模型
from .models import *

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

def add_f(request):
    ## 完成 对一对多关系的 增加操作
    ## 增加出版社数据
    # Publish.objects.create(name="北京出版社",address="北京")
    # Publish.objects.create(name="上海出版社",address="上海")
    # Publish.objects.create(name="深圳出版社",address="深圳")

    ## 增加书
    ## 第一种增加的方法
    # Book.objects.create(name="python入门",pub_id=2)
    #     # 第二种
    ## 正向 从外键所在的表到关联表
    # publish_obj = Publish.objects.filter(name="上海出版社").first()
    # Book.objects.create(name="python全栈", pub=publish_obj)
    Book.objects.create(name="pythonAi",pub=Publish.objects.filter(name="上海出版社").first())


    ## 反向 从关联表到外键所在的表
    ## 拿到 publish的对象
    publish_obj = Publish.objects.filter(name="深圳出版社").first()
    publish_obj.book_set.create(name = "python web")

    return HttpResponse("一对多关系增加操作")

def get_f(request):
    ## 进行一对多关系的查询
    ## 查询北京出版社的书
    # publish_obj = Publish.objects.filter(name="北京出版社").first()
    # publish_obj.book_set.create(name="python 爬虫")
    # publish_obj = Publish.objects.filter(name="北京出版社").first()
    # book_obj = Book.objects.filter(pub_id= publish_obj.id).all()
    # print(book_obj)
    ## 查询 python入门 属于哪个出版社、
    # book_obj = Book.objects.filter(name="python入门").first()
    # pub_obj = Publish.objects.filter(id=book_obj.pub_id).first()
    # print(pub_obj.name)



    ## 正向  从外键所在的表到关联表
        # 查询 python入门 属于哪个出版社、
    # book_obj = Book.objects.filter(name="python入门").first()
    # publish_obj = book_obj.pub
    # print(publish_obj)
    # print(publish_obj.name)
    ## 反向  从关联表到外键所在的表
        # 查询北京出版社的书
    publish_obj = Publish.objects.filter(name="北京出版社").first()
    book_obj = publish_obj.book_set.values("name")
    print(book_obj)

    return HttpResponse("一对多关系的查询")


def update_f(request):
    ## 一对多关系的修改
    ## update
    ## 使用 obj.id
    # pub_obj = Publish.objects.filter(name='深圳出版社').first()
    # Book.objects.filter(name="python全栈").update(pub_id=pub_obj.id)
    ## 正向
    ## 修改书籍的出版社
    # pub_obj = Publish.objects.filter(name="上海出版社").first()
    # book_obj = Book.objects.filter(name="python入门").update(pub = pub_obj)
    # book_obj = Book.objects.filter(name="python入门").update(pub = Publish.objects.filter(name="上海出版社").first())
    ## set
    ## 反向
    # publish_obj = Publish.objects.filter(name="北京出版社").first()
    # book_obj = Book.objects.filter(name="python入门").first()
    # publish_obj.book_set.set([book_obj])
    #

    publish_obj = Publish.objects.filter(name="上海出版社").first()
    book_obj1 = Book.objects.filter(name="python全栈").first()
    book_obj2 = Book.objects.filter(name="python web").first()
    publish_obj.book_set.set([book_obj1,book_obj2])

    return HttpResponse("一对多关系的修改")


def delete_f(request):
    ## 删除
    ## 由于设置了 on_delete=models.CASCADE 在删除关联表数据时，从表中关联数据也会被删除掉
    # Publish.objects.filter(name="上海出版社").delete()
    Book.objects.filter(name="python全栈").delete()


    return HttpResponse("一对多关系的删除")

## 多对多 增加
def add_many(request):
    ## 增加同学
    # Person.objects.create(name="小二",age=20)
    # Person.objects.create(name="小三",age=23)
    # Person.objects.create(name="小四",age=22)
    # Person.objects.create(name="小五",age=24)
    ## 增加teacher
    # Teacher.objects.create(name="老边",gender=1,age=43)
    # Teacher.objects.create(name="老宋",gender=0,age=23)

    # 多对多关系的增加操作
    ## create
    ## 新增数据  并且创建关系
    ## 正向
    ## 老王老师  小白（新同学）
    # teacher_obj =Teacher.objects.filter(name="老王").first()
    # print(teacher_obj)
    # teacher_obj.person.create(name="小白",age=17)
    ## 反向
    # person_obj = Person.objects.filter(name="小李").first()
    # person_obj.teacher_set.create(name="老李",gender=1,age=53)

    ## add   针对已经存在的数据 创建关系
    ## 正向
    ##
    teacher_obj = Teacher.objects.filter(name="老边").first()
    person_obj = Person.objects.filter(name="小二").first()
    teacher_obj.person.add(person_obj)

    teacher_obj = Teacher.objects.filter(name="老边").first()
    person_obj1 = Person.objects.filter(name="小三").first()
    person_obj2 = Person.objects.filter(name="小四").first()
    teacher_obj.person.add(person_obj1,person_obj2)

    ## 反向
    person_obj = Person.objects.filter(name="小五").first()
    teacher_obj = Teacher.objects.filter(name="老宋").first()
    person_obj.teacher_set.add(teacher_obj)







    return HttpResponse("多对多")

## 多对多 查询
def get_many(request):
    # 正向
    ## 老边 交过的学生
    # teacher_obj = Teacher.objects.filter(name="老边").first()
    # person_obj = teacher_obj.person.all().values("name")  ## first values
    # print(person_obj)
    # 反向
    ## 小二 的老师
    person_obj = Person.objects.filter(name="小二").first()
    teacher_obj = person_obj.teacher_set.all()
    print(teacher_obj)

    return HttpResponse("多对多 查询")

## 多对多 修改
def update_many(request):
    ## set
    ## 正向
    ## 老边   将id为2 的学生 学习 老边的课程
    # teacher_obj = Teacher.objects.filter(name="老边").first()
    # person_obj1 = Person.objects.filter(name="小三").first()
    # person_obj2= Person.objects.filter(name="小四").first()
    # person_obj3 = Person.objects.filter(name="小五").first()
    # teacher_obj.person.set([person_obj1,person_obj2,person_obj3])

    ## 反向
    person_obj = Person.objects.filter(name="小五").first()
    # teacher_obj = Teacher.objects.filter(name="老王").first()
    # person_obj.teacher_set.set([teacher_obj])
    ## 可以直接放id 值
    person_obj.teacher_set.set([1,2,3])

    return HttpResponse("多对多 修改")

## 多对多 删除
def delete_many(request):
    ## remove
    ## 正向
    ## 消除  teacher_id = 1 和  person_id = 2 之间的关系
    # teacher_obj = Teacher.objects.get(id = 1)
    # person_obj = Person.objects.get(id = 2)
    # teacher_obj.person.remove(person_obj)
    ## 反向
    #  消除  teacher_id = 1 和  person_id = 6 之间的关系
    # teacher_obj = Teacher.objects.get(id = 2)
    # person_obj = Person.objects.get(id = 1)
    # person_obj.teacher_set.remove(teacher_obj)

    ## clear
    ## 正向
    ## 消除teacher_id = 3 数据的关系、
    # teacher_obj = Teacher.objects.get(id =3)
    # teacher_obj.person.clear()
    ## 反向
    #  消除 person_id = 6 的关系
    # person_obj = Person.objects.get(id = 6)
    # person_obj.teacher_set.clear()
    ##  delete
    ## 删除  person_id = 3
    # Person.objects.filter(id = 3).delete()
    Teacher.objects.filter(id = 3).delete()

    return HttpResponse("多对多 删除")

## 导包
from django.db.models import Sum,Avg,Max,Min,Count,F,Q
def PersonOrm(request):
    ## 聚合查询
    # 返回  字典
    ## key  默认生成的  计算的字段__使用的聚合方法
    ## value   计算的结果
    # data = Person.objects.all().aggregate(Max("age"),Min("age"))
    # print(data)     ##   {'age__max': 24}
    # print(data["age__max"])
    # data = Person.objects.all().aggregate(max_age = Max("age"),sum_age = Sum("age"))
    # print(data)   #  {'max_age': 24}

    # Book.objects.create(name="python",pub_id=3,num=100,price=129)
    # Book.objects.create(name="python1",pub_id=3,num=189,price=159)
    # Book.objects.create(name="python2",pub_id=3,num=40,price=529)
    # Book.objects.create(name="python3",pub_id=3,num=780,price=539)
    # Book.objects.create(name="python4",pub_id=3,num=30,price=595)
    # Book.objects.create(name="python5",pub_id=3,num=20,price=12)
    # Book.objects.create(name="python6",pub_id=3,num=90,price=90)
    # F
    #  能够比较同一张表中的两个字段的大小
    ## 查询 num 大于 price 的书名
    data = Book.objects.filter(num__gt=F("price")).values("name")
    print(data)
    ## 查询 num 大于等于  price * 2 的书名
    data = Book.objects.filter(num =F("price")+ 100).values("name")
    print(data)

    Book.objects.filter(num__gt=F("price")+ 100).delete()

    # Q
    # 能够 实现  and or not 关系
    ## 查询条件为：  num > 10 and price > 10
    # data = Book.objects.filter(num__gt=10,price__gt=10).all()
    ## and 关系 &
    data = Book.objects.filter(Q(num__gt=10) & Q(price__gt=10)).all()
    ## or 关系 |
    data = Book.objects.filter(Q(num__gt=10) | Q(price__gt=10)).all()
    ## not ~
    data = Book.objects.filter(~Q(num__gt=10)).all()

    return HttpResponse("聚合和FQ对象")














# 项目的 视图文件
from lou import app
from flask import render_template
from lou.models import *


@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/courses/")
def courses():
    return render_template("courses.html")


@app.route("/onetable/")
def onetable():
    ##单表操作
    ## 增加数据
    ## 增加单条
    # 第一种
    # c = Course(name="pythonweb",description="pythonweb课程")
    # db.session.add(c)
    # db.session.commit()
    # # 第二种
    # c = Course()
    # c.name="python爬虫"
    # c.description = "python爬虫课程"
    # db.session.add(c)
    # db.session.commit()
    # ## 增加多条
    # c1 = Course(name="pythonweb1", description="pythonweb课程1")
    # c2 = Course(name="pythonweb2", description="pythonweb课程2")
    # c3 = Course(name="pythonweb3", description="pythonweb课程3")
    # c4 = Course(name="pythonweb4", description="pythonweb课程4")
    # db.session.add_all([c1,c2,c3,c4])
    # db.session.commit()

    ## 单表 查询
    # 1、 all   返回所有的数据  返回值为列表
    # c = Course.query.all()
    # print(c)
    # for one in c:
    #     print(one.name)

    # # 2、 get  只能通过id 进行查询
    # #   如果有值 返回对象   如果没有值返回None
    # c = Course.query.get(100)
    # print(c)
    # # print(c.name)

    # 3、 filter filter_by
    # 两个方法 功能 一样  都是过滤筛选
    # 区别是用法不一样
    # c = Course.query.filter(Course.name == "pythonweb").all()
    # print(c)
    # c = Course.query.filter_by(name="pythonweb").all()
    # print(c)

    # 4、 first
    ## 返回第一条数据
    ## 返回类型为对象
    ## 如果没有数据  返回 None
    # c = Course.query.filter(Course.name=="pythonweb").all()
    # print(c)
    # c = Course.query.filter(Course.name=="pythonweb").first()
    # print(c)

    # 5、 order_by   排序
    ## 升序
    # c = Course.query.filter(Course.name=="pythonweb").order_by(Course.id).all()
    # print(c)
    #
    # ## 降序
    # c = Course.query.filter(Course.name=="pythonweb").order_by(Course.id.desc()).all()
    #
    # print(c)

    #6、 分页
    # limit 返回的数据的条数
    # # offset   偏移  以下标进行偏移  从 0开始
    # c = Course.query.limit(2).all()
    # print(c)
    # ## 从 xxx 开始 获取 xxx条数据
    # c = Course.query.offset(100).limit(100).all()
    # print(c)

    ## 修改
    # c = Course.query.get(3)
    # c.name = "python1"
    # db.session.commit()

    ## 删除
    # c = Course.query.get(3)
    # db.session.delete(c)
    # db.session.commit()

    ## 增加
    c = Course(name="python",description="python课程")
    c.save()
    # 更改
    c = Course.query.get(7)
    c.name = "python00001"
    c.update()
    ## 删除
    c = Course.query.get(7)
    c.delete()



    return "单表操作"


@app.route("/onetomany/")
def onetomany():
    ## 一对多
    ## 增加数据
    # 第一种
    # r = Role(r_name="Vip",description="Vip人员")
    # r.save()
    # u = User(name="zhangsan",password="111111",role_id=r.id)
    # u.save()

    # 第二种
    # 从 User -》 role  从另一张模型 到 关系（relationship）所在的模型
    ##   role =对象
    # u = User(name="lisi",password=11111,role = Role.query.get(1))
    # u.save()
    # u = User()
    # u.name="wangwu"
    # u.password = "1111111"
    # u.role = Role.query.filter_by(id= 1).first()    ## 对象
    # u.save()

    # 第三种 从role - 》 user  从关系（relationship） 到另一张模型

    # r = Role(r_name="Vip1",description="Vip1人员",user=[User(name="小白",password="111111"),User(name="小灰",password="111111")])
    # r.save()

    ## 将relationship 放在 外键所在的模型
    # user -> role
    # u = User(name="小黑",password="11111",role=Role(r_name="Vip3",description="Vip3"))
    # u.save()
    #
    # # 从 role -》 user
    # r = Role(r_name="Vip4",description="Vip4用户",user = [User(name="小红",password="11111")])
    # r.save()

    ## 增加用户
    # r = Role.query.get(2)
    # u= User(name="乔丹",password="1111",role_id=r.id)
    # u.save()

    ## 使用 relationship 进行设置
    ## 如果role 数据存在
    # u = User(name="麦迪",password="1111",role = Role.query.get(3))
    # u.save()
    ## 如果 role 不存在
    # u = User(name="麦迪",password="1111",role = Role(r_name="vip6",description="vip6"))
    # u.save()

    ## 增加role 数据
    # r = Role(r_name="VVip1",description="VVip",user=[User(name="杜老二",password="11111")])
    # r.save()

    ## 增加 user
    ## role 已经存在
    # u= User(name="库里",password="11111",role=Role.query.get(3))
    # u.save()
    ## 如果 role 不存在
    # u= User(name="库里",password="11111",role=Role(r_name="VVip2",description="VVip2"))
    # u.save()

    ## 增加 role
    # r = Role(r_name="VVIp4",description="VVIp4",user=[User(name="詹姆斯",password="33333")])
    # r.save()


    ## 查询
    # ## 从 user -》 role
    # u= User.query.get(1)     ### 获取user 对象
    # r = u.role     ### 对象
    # print(r)
    #
    #
    # ## 从 role -》 user
    # r = Role.query.get(1)
    # u = r.user    ### 列表
    # print(u)

    ## 多对多增加
    ## 增加用户 同时增加课程
    ## 从relationship 到另外一个模型
    # c1 = Course.query.get(1)
    # c2 = Course.query.get(2)
    # u= User()
    # u.name = "戴维斯"
    # u.password = "1111"
    # u.role_id = 1
    # u.course = [c1,c2]
    # u.save()

    ##  从另外一个模型 到 relationship
    # u1 = User.query.get(11)
    # u2 = User.query.get(10)
    # c = Course()
    # c.name = "python0000001"
    # c.description = "python0000001"
    # c.user = [u1,u2]
    # c.save()
    ## 绑定关系
    # c = Course.query.get(2)
    # c.user = [User.query.get(3),User.query.get(5)]
    # c.update()

    ##  从user 查到 course
    u = User.query.get(15)
    c = u.course    ### 列表
    print(c)

    ## 从 course -》 user
    c = Course.query.get(2)
    u = c.user  ## 列表
    print(u)

    ## 一对一
    r = Role.query.get(1)
    u = r.user
    print(u)


    c = Course()
    c.name = "python"
    c.description = "python"
    c.addcourse()

    return "一对多操作"
from sqlalchemy import and_,or_,not_,func
@app.route("/gj/")
def gj():
    # ## 逻辑关系
    # data = User.query.filter(User.name=="python",User.password == "11111").all()   ## and
    # print(data)
    # # and_
    # data = User.query.filter(and_(User.name=="python",User.password == "11111")).all()   ## and
    # print(data)
    # # or_
    # data = User.query.filter(or_(User.name=="python",User.password == "11111")).all()   ## or
    # print(data)
    # # not_
    # data = User.query.filter(not_(User.name=="python")).all()   ## not
    # print(data)
    # ## !=
    # data = User.query.filter(User.name != "python").all()
    # print(data)
    # ## >
    # data = User.query.filter(User.id > 9).all()
    # print(data)
    ## 开头
    # data = User.query.filter(User.name.startswith("zh")).all()
    # print(data)
    # # 结束
    # data = User.query.filter(User.name.endswith("黑")).all()
    # print(data)

    # 模糊查询   like
    #   sql 中 _ %
    # data = User.query.filter(User.name.like("%sa%")).all()
    # print(data)
    # data = User.query.filter(User.name.like("%{}%".format("a"))).all()
    # print(data)
    #
    # data = User.query.filter(User.name.like("%%%s%%" % ("a"))).all()    ## %a%
    # print(data)
    #
    # data = User.query.filter(User.name.like("_i%")).all()
    # print(data)
    ## 查询指定字段

    # data = User.query.filter(User.name.like("_i%")).all()  ## select * from ****
    # print(data)
    ## select name from User；
    # data = User.query.all()    ### select * from user;
    # print(data)
    # data = db.session.query(User.name).all()    ## select name from user;
    # print(data)
    # data = db.session.query(User.name,User.password).filter(User.id > 9).all()
    # print(data)

    # data = db.session.query(User.name,func.count(User.id),func.sum(User.id)).group_by(User.name).all()
    # print(data)
    # print(data[0][0])
    try:
        r = Role()
        r.r_name = "VVVip"
        r.description = "VVVip"
        # r.save()
        db.session.add(r)
        # db.session.commit()
        db.session.flush()
        u = User()
        u.name = "李白"
        u.password = "1111111"
        u.role_id = 10000
        # u.save()
        db.session.add(u)
        db.session.commit()
    except:
        print("1111111")
        db.session.rollback()






    return "高级"



# 模型
# from main import db
from blueprintproject import db
class Model(db.Model):
    __abstract__ = True     ### 表名这个类为  抽象类
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        ## 完成保存数据
        db.session.add(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()

## 关系表
user_course = db.Table(
    "user_course",      ###   表名
    db.Column("id",db.Integer,primary_key=True,autoincrement=True),     ###  id 主键    可选项
    db.Column("user_id",db.Integer,db.ForeignKey("user.id")),    #####   用户表外键
    db.Column("course_id",db.Integer,db.ForeignKey("course.id"))     ### 课程表的外键
)

## 创建模型
class User(Model):
    name = db.Column(db.String(32))    ### 用户名
    password = db.Column(db.String(32))  ## 密码
    role_id = db.Column(db.Integer,db.ForeignKey("role.id"))
    picture = db.Column(db.String(64),default="1")    ### 图片
    # role_id = db.Column(db.Integer)
    # role = db.relationship("Role",backref="user")
    course = db.relationship("Course",secondary=user_course,backref="user")
## 角色表
class Role(Model):
    r_name = db.Column(db.String(32))  ## 角色名字
    description = db.Column(db.String(32))   ## 角色描述
    ## relationship  模型间的一种关系 ，user只是代表关系，并不会表现在数据库中
    ## User 关联模型的类名
    ## backref 反向映射
    user = db.relationship("User",backref="role")

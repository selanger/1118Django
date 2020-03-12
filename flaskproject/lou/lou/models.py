from lou import db

class Model(db.Model):
    __abstract__ = True     ### 表名这个类为  抽象类
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
## create table user(id int,name varchar(32),role_id int,foreign key role_id reference role(id));
## 创建模型
class User(Model):
    name = db.Column(db.String(32))    ### 用户名
    password = db.Column(db.String(32))  ## 密码
    role_id = db.Column(db.Integer,db.ForeignKey("role.id"))
    # role_id = db.Column(db.Integer)
    # role = db.relationship("Role",backref="user")

## 角色表
class Role(Model):
    r_name = db.Column(db.String(32))  ## 角色名字
    description = db.Column(db.String(32))   ## 角色描述
    ## relationship  模型间的一种关系 ，user只是代表关系，并不会表现在数据库中
    ## User 关联模型的类名
    ## backref 反向映射
    user = db.relationship("User",backref="role")

class Course(Model):
    name = db.Column(db.String(32))   ## 课程名字
    description = db.Column(db.String(32))  ## 课程描述
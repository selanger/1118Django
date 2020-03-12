## 数据库配置
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
# import pymysql
# pymysql.install_as_MySQLdb()

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
## 增加配置
## 链接 sqllit 数据库
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" +(os.path.join(BASE_DIR,"flask.db"))
## 配置链接mysql   mysql://用户名：密码@mysql服务器ip/库名
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:111111@localhost/flaskdemo"
## 自动跟踪 修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
## 打印生成的sql  常用于调试模式
# app.config["SQLALCHEMY_ECHO"] = True

## 绑定app 和sqlalchemy
db = SQLAlchemy(app)

class Model(db.Model):
    __abstract__ = True     ### 表名这个类为  抽象类
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
## 创建模型
class User(Model):
    ## 模型 不会像django模型中 自动创建id 主键
    # id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32))

class Course(Model):
    # id  = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32))
## 数据迁移   同步表结构
## db.create_all() 方法  只能将新创建的模型进行同步，不管模型中是发生属性变更还是类型变更 ，都不会同步
db.create_all()



if __name__ == '__main__':
    app.run()





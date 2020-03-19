from main import db
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

class Label(Model):
    name = db.Column(db.String(32))      ### 标签名字
    description = db.Column(db.Text)     ## 标签描述
    course = db.relationship("Course",backref ="label")

class Course(Model):
    name = db.Column(db.String(32))   ## 课程名字
    description = db.Column(db.String(32))  ## 课程描述
    picture = db.Column(db.String(64),default="1.jpg")     ## 图片
    show_number = db.Column(db.Integer)     ##  观看人数
    status = db.Column(db.Integer,default=1)       ## 状态 1代表已上线  0 代表未上线
    type = db.Column(db.Integer,default=1)       ## 类别  1代表 免费 2 代表限免 3代表vip
    time_number = db.Column(db.Integer)       ## 课时
    lebal_id = db.Column(db.Integer,db.ForeignKey("label.id"))
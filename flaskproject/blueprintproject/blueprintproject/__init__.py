### 项目的初始化文件
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def createApp(obj):
    ## 创建app  初始化app
    app = Flask(__name__)
    app.config.from_object(obj)
    ## 绑定app 和sqlalchemy
    # db = SQLAlchemy(app)
    db.init_app(app)     ### 惰性加载
    from blueprintproject.course import course_bl
    from blueprintproject.user import user_bl
    app.register_blueprint(course_bl, url_prefix="/course")
    app.register_blueprint(user_bl, url_prefix="/user")

    return app




















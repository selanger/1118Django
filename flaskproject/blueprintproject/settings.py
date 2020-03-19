## 配置文件
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:111111@localhost/lou"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# app.config["SQLALCHEMY_ECHO"] = True
import os
class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:111111@localhost/lou1"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_ECHO = True
    DEBUG = True
    STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')
    SECRET_KEY = "dhfsdjkaf"


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:111111@localhost/lou"
    DEBUG = False





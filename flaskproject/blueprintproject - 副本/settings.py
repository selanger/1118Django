## 配置文件

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:111111@localhost/lou7"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_ECHO = True
    DEBUG = False
    SECRET_KEY = "dhfsdjkaf"


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:111111@localhost/lou"
    DEBUG = False





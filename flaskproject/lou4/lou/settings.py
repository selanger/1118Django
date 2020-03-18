## 配置文件
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:111111@localhost/lou"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# app.config["SQLALCHEMY_ECHO"] = True

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:111111@localhost/lou"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_ECHO = True
    DEBUG = False

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:111111@localhost/lou"
    DEBUG = False





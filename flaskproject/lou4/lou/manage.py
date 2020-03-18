## 项目的 控制文件
# from lou import app
from lou.views import app
# from lou import db
from lou.models import db
if __name__ == '__main__':
    db.create_all()
    print(app.config)
    app.run()
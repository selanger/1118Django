### 项目的控制文件
from blueprintproject import createApp
app = createApp("settings.Config")

if __name__ == '__main__':
    # from course.models import *
    # from user.models import *
    # db.create_all()
    app.run(debug=True)










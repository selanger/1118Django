### 项目的控制文件
from blueprintproject import createApp
from flask_script import Manager,Command
from flask_migrate import MigrateCommand
app = createApp("settings.Config")
## 管理app
manager = Manager(app)
class Hello(Command):   ## 自定义命令   需要继承 Command父类
    def run(self):     ## 重写run方法
        ### 命令执行内容
        print("HELLO world")
### python manage.py runsever8000   项目启动在 127.0.0.1:8000 端口
class Runserver(Command):
    def run(self):
        app.run(port=8000)

manager.add_command("hello",Hello)    ### 添加命令  第一个参数： 命令的名字  第二个参数： 命令的内容
manager.add_command("runserver8000",Runserver)
manager.add_command("db",MigrateCommand)
if __name__ == '__main__':
    # from course.models import *
    # from user.models import *
    # db.create_all()
    # app.run(debug=True)
    manager.run()










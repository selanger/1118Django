from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
from course import course_bl
from user import user_bl
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config.from_object("settings.Config")
## 绑定app 和sqlalchemy
db = SQLAlchemy(app)
STATICFILES_DIRS = os.path.join(BASE_DIR,'static')


app.register_blueprint(course_bl,url_prefix="/coruse")
app.register_blueprint(user_bl,url_prefix="/user")
if __name__ == '__main__':
    from course.models import *
    from user.models import *
    db.create_all()
    app.run(debug=True)










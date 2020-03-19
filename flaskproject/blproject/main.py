from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("settings.Config")
db = SQLAlchemy(app)
from user import user_bl
from course import course_bl
app.register_blueprint(user_bl,url_prefix="/user")
app.register_blueprint(course_bl,url_prefix="/course")


if __name__ == '__main__':
    # from user.models import *
    # from course.models import *
    db.create_all()
    app.run()
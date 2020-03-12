# 项目的 视图文件
from lou import app
from flask import render_template


@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/courses/")
def courses():
    return render_template("courses.html")
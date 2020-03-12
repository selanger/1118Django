from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/courses/")
def courses():
    return render_template("courses.html")



if __name__ == '__main__':
    app.run(debug=True)










from user import user_bl



@user_bl.route("/index/")
def index():
    return "index"

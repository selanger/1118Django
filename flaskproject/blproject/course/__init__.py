from flask import Blueprint
course_bl = Blueprint("course",__name__,static_folder="static")
from course.views import *

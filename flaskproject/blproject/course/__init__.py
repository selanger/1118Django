from flask import Blueprint
course_bl = Blueprint("course",__name__)
from course.views import *

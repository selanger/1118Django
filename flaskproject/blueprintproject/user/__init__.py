from flask import Blueprint

user_bl = Blueprint("user",__name__)
from user.views import *
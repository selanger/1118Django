## 编写自定义过滤器
# 1. 导包
from django import template
# 2. 实例化对象
register = template.Library()

## 前端调用
##  {{ age | myadd}}   age = 12 -> 12+12=24
## 编写过滤器方法
@register.filter(name="MyAdd")
def myadd(num):
    return num + num
## {{ age | my_two_add:12}}
@register.filter()
def my_two_add(num1,num2):
    return num1+num2
## 调用方式
## {% mymanyadd 10 10 10 10 %}
@register.simple_tag()
def mymanyadd(a,b,c,d):
    result = a + b + c +d
    return result


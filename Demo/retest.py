"""
正则：  是一种字符串的处理方式，用于字符串匹配的
字符串的匹配分为两种：
    内容匹配：
        例如：python中的re模块，js中的匹配
        通过要匹配的内容的类型，长度进行匹配的
    结构匹配：

        xpath 获取到内容的某个标签进行匹配
        通过获取内容在这个文档中的结构，进行匹配
    内容匹配的类型：
        类型匹配
            原样匹配 . \d \D \w \W [] | ()
        长度匹配
            * + ? {}
        特殊匹配
            ^ $
"""
import re
# re.findall()   以列表的形式，尽可能返回结果
str = "hello \n \t world _____ 123"
# 原样匹配
# res = re.findall("hello",str)
# print (res)    # ['hello']
#  . 除了 \n 的所有内容
# res = re.findall(".",str)
# print(res)
# \d  匹配数字
# res = re.findall("\d",str)
# print(res)
# # \D 匹配的是  除了数字
# res = re.findall("\D",str)
# print(res)
# \w   匹配  字母 数字  下划线
# res = re.findall("\w",str)
# print(res)
# \W   匹配 非字母  非数字 非下划线
# res = re.findall("\W",str)
# print(res)
# []   返回符合括号中的内容
# res = re.findall("[a-zA-Z1-9]",str)
# print(res)
# |  匹配任意一边的内容
# res = re.findall("hello|world",str)
# print (res)
#】
str = "444 564"
res = re.findall("(\d)4",str)
print(res)
# str = "hllo \n \t world _____ 123"
# ()  组  组匹配 将括号外面的内容，当做条件进行匹配
## 捕获
## ll  原因： re.findall()  匹配所有的不重叠的匹配成功的部分
# res = re.findall("(\w)l",str)
# print(res)
# str = "123 444 554"
##  str = 13  14  356 34
# str = "5y 7y 8y 9x"
# res = re.findall("(\d)y",str)
# print (res)

## 组匹配  起 组名
## (?P<id>\d) 起组名  组名叫id
# res = re.findall("(?P<id>\d)4",str)
# print (res)    ## 4  5
## 调用组名的内容
# # ## (?P=id) 代表 使用前面的匹配结果
# # # res = re.findall("(?P<id>\d)4(?P=id)",str)
# # # print (res)           id=3

# 长度匹配
str = "hello \n \t world _____ 123"
# * 匹配 0个或者多个
# res = re.findall("\d*",str)
# print (res)
# + 匹配一个或者多个
# res = re.findall("\d+",str)
# print (res)
# ? 匹配 0和  或者1个
# res = re.findall("\d?",str)
# print(res)
# {} 匹配多次，匹配{} 内指定的次数
# res = re.findall("\d{1}",str)
# print(res)
# 特殊匹配
# ^ 匹配 以什么开头
str = "hello \n \t world _____ 123"
res = re.findall("^hello",str)
print(res)
# $ 匹配 以什么结束
res = re.findall("123$",str)
print(res)

































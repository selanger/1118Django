# import functools
# def outer(func):
#     @functools.wraps()
#     def inner(*args,**kwargs):
#         print("22222")
#         return func(*args,**kwargs)
#     return inner
# def outer1(func):
#     def inner(*args, **kwargs):
#         print("3333")
#         return func(*args, **kwargs)
#     return inner
# @outer
# # @outer1    ## demo = outer1(demo)
# def demo():
#     print(1111)
#     return "hello"
# @outer
# def demo02():
#     return "hello02"
#
# res = demo()
# print(res)
# res = demo02()
#
#
#
#
#

for i,j in enumerate(range(10),100):
    print(i)   ## 下标
    print(j)   ## range 生成的值
    print(str(i).zfill(6))


import random

print(round(random.random()*100,2))




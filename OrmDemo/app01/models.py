from django.db import models

# Create your models here.

class User(models.Model):
    ## 写属性
    ## 主键 id   django的ORM 会自动创建一个id 主键
    # id = models.AutoField(primary_key=True)    ## 主键
    user_name = models.CharField(max_length=32)             ### 字符串
    age = models.IntegerField()                ## int 类型
    phone = models.CharField(max_length=11)
    email = models.EmailField(default="111@qq.com")







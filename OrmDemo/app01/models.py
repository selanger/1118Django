from django.db import models

# Create your models here.

class User(models.Model):
    ## 写属性
    ## 主键 id   django的ORM 会自动创建一个id 主键
    # id = models.AutoField(primary_key=True)    ## 主键
    user_name = models.CharField(max_length=32,verbose_name="用户名")             ### 字符串
    age = models.IntegerField(verbose_name="年龄")                ## int 类型
    phone = models.CharField(max_length=11,verbose_name="手机号")   ## 手机号
    email = models.EmailField(default="111@qq.com",verbose_name="邮箱")

    # def __str__(self):
    #     return self.user_name

    class Meta:
        db_table = "user"
        # ordering = ["age","-id"]   ## 决定返回的数据的排序结果
        verbose_name_plural = "用户"



class Subject(models.Model):
    name = models.CharField(max_length=32,verbose_name="学科的名字")
    start_time = models.DateField(verbose_name="开始时间")
    class Meta:
        db_table = "subject"  # 修改表的名字
        verbose_name = "学科"   ## 修改中文  1. 站点管理中展示的名字  2。 对表进行备注
        verbose_name_plural = "学科"   # 去掉复数显示

class Publish(models.Model):
    name = models.CharField(max_length=32,verbose_name="出版社名字")
    address = models.CharField(max_length=32,verbose_name="出版社地址")
    class Meta:
        db_table = "publish"  ## 表名
        verbose_name_plural = "publish"


class Book(models.Model):
    name = models.CharField(max_length=32,verbose_name="书名")
    pub = models.ForeignKey(to=Publish,to_field="id",on_delete=models.CASCADE)
    num = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    ## pub 外键创建好之后，表中表现为  pub_id
    class Meta:
        db_table = "book"
        verbose_name_plural="book"

    ## to 代表 和那个表产生关联
    ## to_field 代表和关联表中的那个字段进行关联，可以不填，不填默认使用关联表的id
    # on_delete  代表当关联表（publish）中的数据被删除的时候，Book表要做什么行为
        # models.CASCADE 默认删除，当关联表中数据删除之后，要删除
        # models.PROTECT 保护的

class Person(models.Model):
    name = models.CharField(max_length=32,verbose_name="学生姓名")
    age = models.IntegerField(verbose_name="年龄")
    class Meta:
        db_table="person"
class Teacher(models.Model):
    name = models.CharField(max_length=32,verbose_name="老师姓名")
    gender = models.IntegerField(verbose_name="性别")   ### 1 代表 男， 0代表 女
    age = models.IntegerField(verbose_name="年龄")
    person = models.ManyToManyField(to=Person)
    class Meta:
        db_table = "teacher"




















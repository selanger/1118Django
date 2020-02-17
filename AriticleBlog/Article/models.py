from django.db import models

# Create your models here.


GENDER_STATUS = (
    (0,"女"),
    (1,"男")
)


class Author(models.Model):
    name = models.CharField(max_length=32,verbose_name="作者姓名")
    # gender = models.CharField(max_length=32,verbose_name="性别")    ### 男  女
    gender = models.IntegerField(choices=GENDER_STATUS,verbose_name="性别")    ###  1 代表  男  0 代表女
    age = models.IntegerField(verbose_name="年龄")
    email = models.EmailField(verbose_name="邮箱")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "author"

class Type(models.Model):
    name = models.CharField(max_length=32,verbose_name="类型名字")
    description = models.TextField(verbose_name="描述")
    def __str__(self):
        return self.name
    class Meta:
        db_table = "type"

class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name="标题")
    date = models.DateField(auto_now=True,verbose_name="创建时间")
    content = models.TextField(verbose_name="内容")
    description = models.TextField(verbose_name="文章描述")
    author = models.ForeignKey(to=Author,to_field="id",on_delete=models.CASCADE)
    type = models.ManyToManyField(to=Type)
    def __str__(self):
        return self.title
    class Meta:
        db_table = "article"









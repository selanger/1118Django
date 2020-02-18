from django.db import models
from ckeditor.fields import RichTextField
## RichTextField   底层是 TextField  只是修改前端的样式，能够将输入的内容以html的格式进行重新排版






# Create your models here.


GENDER_STATUS = (
    (0,"女"),
    (1,"男")
)


class Author(models.Model):
    name = models.CharField(max_length=32,verbose_name="作者姓名")
    # gender = models.CharField(max_length=32,verbose_name="性别")    ### 男  女
    gender = models.IntegerField(choices=GENDER_STATUS,verbose_name="性别")    ###  1 代表  男  0 代表女
    age = models.IntegerField(null=True,blank=True,verbose_name="年龄")
    ## null = True  在数据库中 是可以为空
    ## blank = True 在表单中是可以为空

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
    content = RichTextField(verbose_name="内容")
    description = RichTextField(verbose_name="描述")
    # content = models.TextField(verbose_name="内容")
    # description = models.TextField(verbose_name="文章描述")
    ## 由   upload_to 决定了图片上传的路径 static/images/
    ##  upload_to  当 images 目录存在的时候，直接将图片上传到iamges 目录下
    ##             当 images 目录不存在的时候，创建images目录并且完成图片的上传
    picture = models.ImageField(upload_to="images",verbose_name="图片")
    recommend = models.IntegerField(default=0,verbose_name="推荐")  ## 0 代表不推荐  1 代表推荐
    click = models.IntegerField(default=0,verbose_name="点击率")
    author = models.ForeignKey(to=Author,to_field="id",on_delete=models.CASCADE)
    type = models.ManyToManyField(to=Type)
    def __str__(self):
        return self.title
    class Meta:
        db_table = "article"



class User(models.Model):
    username = models.CharField(max_length=32,verbose_name="用户名")
    password = models.CharField(max_length=32,verbose_name="密码")
    create_time = models.DateTimeField(auto_now=True,verbose_name="创建时间")
    class Meta:
        db_table="user"









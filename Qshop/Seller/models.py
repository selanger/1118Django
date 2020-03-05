from django.db import models
from django.db.models import Manager

# Create your models here.

GENDER_STATUS = (
    (0,"女"),
    (1,"男")
)

class MyUser(Manager):
    ## 查询
    def getusername(self,id):
        ## 根据 用户id 查询用户邮箱
        ##
        user = LoginUser.objects.filter(id = id).first()
        if user:
            return user.email
        else:
            return user
    def adduser(self,email,password):
        user = LoginUser.objects.filter(email=email).first()
        if user:
            return user.email
        else:
            user = LoginUser.objects.create(email=email, password=password)
            return user.email


class LoginUser(models.Model):
    email = models.EmailField(verbose_name="邮箱")
    password = models.CharField(max_length=32,verbose_name="密码")
    username = models.CharField(max_length=32,verbose_name="用户名",default="")
    phone_number = models.CharField(max_length=11,verbose_name="手机号",null=True,blank=True)
    age = models.IntegerField(verbose_name="年龄",null=True,blank=True)
    gender = models.IntegerField(choices=GENDER_STATUS,verbose_name="性别",default=1)
    address = models.TextField(verbose_name="地址",null=True,blank=True)
    photo = models.ImageField(upload_to="img",default="img/gtl.jpg",verbose_name="图片")
    user_type = models.IntegerField(default=1,verbose_name="用户身份")   ## 0 代表卖家 1代表买家
    objects = MyUser()
    class Meta:
        db_table = "loginuser"

class GoodsType(models.Model):
    type_label = models.CharField(max_length=32,verbose_name="类型标签")
    type_description = models.TextField(verbose_name="类型的描述")
    type_picture = models.ImageField(max_length=64,verbose_name="类型的图片")

    class Meta:
        db_table = "goods_type"

class Goods(models.Model):
    goods_number = models.CharField(max_length=11,verbose_name="商品编号")
    goods_name = models.CharField(max_length=32,verbose_name="商品名字")
    goods_price = models.FloatField(verbose_name="商品价格")
    goods_count = models.IntegerField(verbose_name="商品数量")
    goods_location = models.CharField(max_length=32,verbose_name="商品产地")
    goods_safe_date = models.IntegerField(verbose_name="商品保质期")
    goods_pro_time = models.DateTimeField(auto_now=True,verbose_name="生成日期")
    goods_status = models.IntegerField(verbose_name="商品状态",default=1)   ## 0代表下架  1 代表在售
    goods_picture = models.ImageField(upload_to="img",default="img/1.jpg",verbose_name="商品的图片")
    goods_description = models.TextField(default="good goods",verbose_name="商品的描述")
    goods_type = models.ForeignKey(to=GoodsType,on_delete=models.CASCADE)
    goods_store = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)

    class Meta:
        db_table = "goods"


class ValidCode(models.Model):
    email = models.CharField(max_length=32,verbose_name="用户账号")
    code = models.CharField(max_length=8,verbose_name="验证码")
    create_time = models.DateTimeField(auto_now=True,verbose_name="验证码创建时间")


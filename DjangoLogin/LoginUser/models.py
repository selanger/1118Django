from django.db import models

# Create your models here.

GENDER_STATUS = (
    (0,"女"),
    (1,"男")
)

class LoginUser(models.Model):
    email = models.EmailField(verbose_name="邮箱")
    password = models.CharField(max_length=32,verbose_name="密码")
    phone_number = models.CharField(max_length=11,verbose_name="手机号",null=True,blank=True)
    age = models.IntegerField(verbose_name="年龄",null=True,blank=True)
    gender = models.IntegerField(choices=GENDER_STATUS,verbose_name="性别",default=1)
    address = models.TextField(verbose_name="地址",null=True,blank=True)

    class Meta:
        db_table = "loginuser"



class Goods(models.Model):
    goods_number = models.CharField(max_length=11,verbose_name="商品编号")
    goods_name = models.CharField(max_length=32,verbose_name="商品名字")
    goods_price = models.FloatField(verbose_name="商品价格")
    goods_count = models.IntegerField(verbose_name="商品数量")
    goods_location = models.CharField(max_length=32,verbose_name="商品产地")
    goods_safe_date = models.IntegerField(verbose_name="商品保质期")
    goods_pro_time = models.DateTimeField(auto_now=True,verbose_name="生成日期")
    goods_status = models.IntegerField(verbose_name="商品状态",default=1)   ## 0代表下架  1 代表在售

    class Meta:
        db_table = "goods"


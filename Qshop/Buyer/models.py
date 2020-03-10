from django.db import models
from Seller.models import LoginUser,Goods

# Create your models here.

ORDER_STATUS = (
    (1,"未支付"),
    (2,"已支付"),
    (3,"待发货"),
    (4,"已发货"),
    (5,"拒收"),
    (6,"已完成"),
)
class PayOrder(models.Model):
    order_number = models.CharField(max_length=36,unique=True,verbose_name="订单号")
    order_date = models.DateField(auto_now=True,verbose_name="订单创建时间")
    order_status = models.IntegerField(choices=ORDER_STATUS,verbose_name="订单状态")
    order_total = models.FloatField(verbose_name="订单总价")
    order_user = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,verbose_name="买家")
    class Meta:
        db_table = "pay_order"

class OrderInfo(models.Model):
    order = models.ForeignKey(to=PayOrder,on_delete=models.CASCADE)
    goods = models.ForeignKey(to=Goods,on_delete=models.CASCADE)
    goods_price = models.FloatField(verbose_name="商品的单价")
    store = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,verbose_name="卖家")
    goods_count = models.IntegerField(verbose_name="购买的单品的数量")
    goods_total_price = models.FloatField(verbose_name="购买的单品的总金额")
    class Meta:
        db_table = "order_info"


class Cart(models.Model):
    goods = models.ForeignKey(to=Goods,on_delete=models.CASCADE)
    goods_number = models.IntegerField(verbose_name="商品的数量")
    goods_total = models.FloatField(verbose_name="商品的小计")
    # goods_price = models.FloatField()
    cart_user = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,verbose_name="买家")
    class Meta:
        db_table = "cart"

class UserAddress(models.Model):
    name = models.CharField(max_length=32,verbose_name="收货人姓名")
    phone = models.CharField(max_length=11,verbose_name="收货人手机号")
    address = models.TextField(verbose_name="收货人手机号")
    user = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)
    status = models.IntegerField(verbose_name="地址状态",default=0)  ### 1 为使用中  0为 未使用

class PayorderAddress(models.Model):
    name = models.CharField(max_length=32,verbose_name="收货人姓名")
    phone = models.CharField(max_length=11,verbose_name="收货人手机号")
    address = models.TextField(verbose_name="收货人手机号")
    payorder = models.OneToOneField(to=PayOrder,on_delete=models.CASCADE)  ## 一对一




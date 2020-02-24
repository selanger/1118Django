"""
 用来对接口返回的数据  进行序列化
"""

from rest_framework import serializers
from .models import Goods

class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goods  ## 序列化的模型
        fields = ["id","goods_number","goods_name","goods_price","goods_count","goods_location","goods_safe_date","goods_status"]## 决定返回的字段



from .models import LoginUser

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoginUser  ## 序列化的模型
        fields = ["id","email","password","phone_number","age","gender","address"]## 决定返回的字段














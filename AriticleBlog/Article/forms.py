## 编写form表单类
## 导包
from django import forms

## 编写form表单类
# 类名随意
class UserForm(forms.Form):
    username = forms.CharField(max_length=8,label="姓名",required=True)
    password = forms.CharField(max_length=8,min_length=6,label="密码")

    #   max_length 最大长度
    #   min_length  最小长度
    #   required  是否为空，默认为True代表不可为空
    #  label  标签的内容

    ### 固定写法
    def clean_username(self):
        ## 校验数据
        ##获取数据
        username = self.cleaned_data.get("username")
        ## 校验规则
        if username == "admin":
            ## 校验不通过
            self.add_error("username","用户名不能是admin")
        else:
            ## 校验通过
            return username








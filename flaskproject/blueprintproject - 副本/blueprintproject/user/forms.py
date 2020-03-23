### 编写form 类
from flask_wtf import FlaskForm
import wtforms
from wtforms import validators   ### 校验器
from wtforms import ValidationError
### 自定义的校验方法
def check_name(form,field):
    """
    自定义校验      判断敏感字   获取数据库是否存在 等等
    :param form:   表单
    :param field:   字段
    :return:   返回一个异常信息
    """
    print(field.data)   ### 能够获取到数据
    data_list = ["admin","xxx"]     ### 这个中的内容不允许出现在注册账号上
    for one in data_list:
        if one in field.data:
            ### 代表校验不通过
            ## 返回异常
            raise ValidationError("注册账号中不能够有敏感字")
class UserForm(FlaskForm):
    ## 对填写的数据进行校验
    name = wtforms.StringField(
        label="账号",
        ## 校验规则
        validators = [
            validators.DataRequired(message="内容不能为空"),                 ### 必填
            validators.Email(message="必须是邮箱"),                           #### 必须是邮箱格式
            check_name
        ]
    )
    password = wtforms.PasswordField(
        label="密码",
        validators = [
            # validators.NumberRange(1,9999,message="内容必须为数字"),           #### 必须为数字
            validators.Length(min=6,max=8,message="密码为6到8位"),      ###数据的长度
            validators.EqualTo("repassword",message="密码不一致")       ### 和那个字段的内容相等
        ]
    )
    repassword = wtforms.PasswordField(label="密码")
    age = wtforms.IntegerField(
        validators = [
            validators.NumberRange(min=11111,max=99999,message="不在范围之内")
        ]
    )


## StringField 类似于input中的 text
##  PasswordField 类似于 input中的password
## SelectField 类似于 input中的select
## HiddenField    类似于 input中的 hidden
## RadioField    类似于 input中的 radio









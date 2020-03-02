##  支付宝支付 demo
alipay_public_key_string="""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAh5AE4ca3NYqqXy9FLqg2hJgi6SmJrIe4nE+dPmDn6BWW8N+JltCI5A9TMEwMiQyENaCO2XpaZlh5UVi5pJE45Sa2pelmgeN/7M73zLn5UZwPjIwdYpFU+P16yD5IyhQusmB4cKIReT0jkcj0IBCp7Iyb5QugVmgxqgA8svHRKQg3p/aE1e1/HiLxReIFvHg9CUuFUwmJ7dLQ1k4sxgoxzKA/pj99FThptCFu+wA0GUPT3I/T42PoVmf/UZ/fHn7qdLc9TxanvU8sSU7UtXms5m56qqh6H8YgUPlGDVetWU/HR+VAAEJc5RMcXGEHqeqp7NFe9zZhxOr61r4P0HzUrwIDAQAB
-----END PUBLIC KEY-----"""
app_private_key_string="""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAh5AE4ca3NYqqXy9FLqg2hJgi6SmJrIe4nE+dPmDn6BWW8N+JltCI5A9TMEwMiQyENaCO2XpaZlh5UVi5pJE45Sa2pelmgeN/7M73zLn5UZwPjIwdYpFU+P16yD5IyhQusmB4cKIReT0jkcj0IBCp7Iyb5QugVmgxqgA8svHRKQg3p/aE1e1/HiLxReIFvHg9CUuFUwmJ7dLQ1k4sxgoxzKA/pj99FThptCFu+wA0GUPT3I/T42PoVmf/UZ/fHn7qdLc9TxanvU8sSU7UtXms5m56qqh6H8YgUPlGDVetWU/HR+VAAEJc5RMcXGEHqeqp7NFe9zZhxOr61r4P0HzUrwIDAQABAoIBADagcWcttVwtAZSTrtQrUrTBvaepZmIQ2vKaHmopkKn0MTvlSENuywrjpgkbTB3Z3ljh106JwG3njxOZpk1Le9rTa9yVngoPS9h4WmC0PGSHd7iSKbEzkUM4mcahWqGb2mlk+IOiu1nYqkGv8bgOHvtEefmlYroPCJxRtiQBz+AxY7h3nrG4okeV19SAYi60wA9/z49PfoldXVfDos9pMuLTDQmk5xR424Y00Qu2fObAdiwMv4Muhb1hDlmPw7a9ErsSGp6aIUD0dB7EieYuwynUUNaKE/J+V4L8ApNvhvpQK5YDCTA4guRo6T75fsjSekd5SORrtF1/totLxHaULyECgYEA+qMFfOpXOcoA/aGO6z3GZOZlKeZG03QnEpIQ8DAfkyqOWSmu0AyFgZKVvCDqMGPNUMZoGxbyGw83A1aTFnwqdk5tSmnNBxQiMlfOjUNMrPdRAl+i8lV5ymjPToWi/os2mX0gks8YPsmNtPgMIEZ4sJ3eLaojTEjYcKNlPN5IvJ8CgYEAinagIr+/wns+0MBE9qgT3m9OeekF7h5Hqy2xI2QtnpCkLdg4JXblpLh9/UZUeXmP8HSIkNoI41n9RW7qzgTWx83zvIHhqheKeJRKROss5kJtciOUMnOL+XSK43DFAz0KeXz1/HvWdc6OKRx5mz3cPplkUGkwqU+iynW074AS3fECgYEA3Gyk9fAOmFdMucLtM3wX0END8y5/WZZMiquFVAeurTn/CPF8uaJZg9QL9fEopTgQqJplknWCpUOjST9JirvWiEd/HLOhyjjtvkK0+E2Y0IGNcD31y5Ra0SWONGuZJq3+bcy66gJSO139T4va9kOj/whIDvcTphJmr+Eztu1zINcCgYBp7DuuuY9hoNS57wwSwRuKAw4+tqOBuIpNCkRDdcRsU+w04f55so4Ux8oh8iZ3UyZo5Uz/urwn6FSXRDW96ve/m+8EWzud2ipk+dQjCuGrOE/vjAY33irLZ3tEaKVeR9j2fUDUqIu0TZJ1IsJonxcYkFGsLfw62aAIT6ldulU0kQKBgQD2ndjwswgtl7vVetmTqmbDEHR3F43Xz0AtEw6CJyfU9Ai3Sy5rv99a/Qyv9DnW/GlcDp7/fI9C8dnzAbqcRPjHaQrXwpZbQiqTr1gmGypBqV4OuU6LBA5xcgY02vDKXZ7nQC4bCeFjDtIfEjvUXE5Xlc1ILdT1Ghh9hIBAhXjcOQ==
-----END RSA PRIVATE KEY-----"""

# 1、 导包
from alipay import AliPay

# 2、 创建一个实例对象
alipay =AliPay(
    appid="2016101300673550",
    app_notify_url=None,
    app_private_key_string=app_private_key_string,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2",
    debug=False
)

# 3、 实例化一个订单
order_string = alipay.api_alipay_trade_page_pay(
    subject="军火交易",  ## 主题
    out_trade_no="23179523237933",   ## 订单号
    total_amount="777",  ## 交易金额   字符串
    return_url=None,    ##  回调的地址
    notify_url=None     ## 通知
)



# 4、 返回支付宝支付的url
result = "https://openapi.alipaydev.com/gateway.do?" + order_string
print(result)












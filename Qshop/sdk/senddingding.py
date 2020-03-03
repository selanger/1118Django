import requests
import json
data = {
    "msgtype": "text",
    "text": {
        "content": "您的验证码为：1234，打死不要告诉别人！！！"
    },
    "at": {
        "atMobiles": [
            "15833398502"
        ],
        "isAtAll": False
    }
}

### 发送请求
url = "https://oapi.dingtalk.com/robot/send?access_token=2ac50273f914001f90960ce6afc74f4700e2753ff83144fdd0a7324b1b3641f8"
headers = {'Content-Type': 'application/json'}
## 转json
data = json.dumps(data)
resp = requests.post(url,headers = headers,data=data)
print(resp.content.decode())







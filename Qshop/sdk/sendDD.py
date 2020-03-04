import requests
import json
def senddingding(params):
    """
    parmas = {
        "content": "您的验证码为：1234，打死不要告诉别人！！！",
        "atMobiles":[]
        "isAtAll":True/False
    }
    :param params:
    :return:
    """
    data = {
        "msgtype": "text",
        "text": {
            "content": params.get("content")
        },
        "at": {
            "atMobiles": [
                params.get("atMobiles")
            ],
            "isAtAll": params.get("isAtAll")
        }
    }

    ### 发送请求
    url = "https://oapi.dingtalk.com/robot/send?access_token=2ac50273f914001f90960ce6afc74f4700e2753ff83144fdd0a7324b1b3641f8"
    headers = {'Content-Type': 'application/json'}
    ## 转json
    data = json.dumps(data)
    resp = requests.post(url,headers = headers,data=data)
    print(resp.content.decode())

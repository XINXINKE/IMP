import json
import requests
from testcase.method2.gettokenid import SaveTokenid

"""该方法二：就是通过调用获得token和其他id的方法 去拿到这些全局变量"""
t = SaveTokenid()
token, clientid, chatinfoId = t.save_tokenid()
url = "https://customer-inquiry-chat-plus-sit.mercedes-benz.com.cn/api/v1/chatInfo/initChat"
headers = {
    'modeltype': 'modeld',
    "flag": "2",
    "content-type": "application/json",
    "token": token,
    "client-id": str(clientid)
}

data = {"id": clientid,
        "threadId": chatinfoId,
        "showMessage": "true",
        "message": {
            "tmessage": "您好，我是奔驰EQ在线客服~很乐意为您服务，请问有什么可以帮您？",
            "sendTime": "1688440567200"
        }
        }
data = json.dumps(data)
res = requests.post(url=url, data=data, headers=headers)
res = res.json()
print(res)

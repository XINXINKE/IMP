import json

import requests
import jsonpath

url = "https://customer-inquiry-chat-plus-sit.mercedes-benz.com.cn/api/v1/chatInfo/initChat"
headers = {
    'modeltype': 'modeld',
    "flag": "2",
    "content-type": "application/json"}
data = {"id": "${clientId}",
        "threadId": "${chatinfoId}",
        "showMessage": "true",
        "message": {
            "tmessage": "您好，我是奔驰EQ在线客服~很乐意为您服务，请问有什么可以帮您？",
            "sendTime": "1688440567200"
        }
        }
js_data = json.dumps(data)
res = requests.post(url=url, data=js_data, headers=headers)
print(res.status_code)
res = res.json()
print(res)
token = jsonpath.jsonpath(res, "$.data.token")
print(token)

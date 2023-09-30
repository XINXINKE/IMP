import json
import requests
from common.parser_file import Yamlfile

"""方法一：该请求通过读取yaml文件的token和id并发送请求"""
dict = Yamlfile()
dict1 = dict.file_read(r"D:\liukexin\IM0905\code\common\token.yml")

token = dict1["token"]  # 提取yaml文件中的token参数
clientid = dict1["clientid"]  # 提取yaml文件中的clientid参数
chatinfoId = dict1["chatinfoId"]  # 提取yaml文件中的chatinfoId参数
"""token = json.dumps(token)  # 将python数据结构转化成json字符串
clientid = json.dumps(clientid)
chatinfoId = json.dumps(chatinfoId)"""
print(token)  # 此时打印出来的token为列表 list
print(clientid)  # 此时打印出来的clientid为列表 list
print(chatinfoId)  # 此时打印出来的chatinfoId为列表 list
print(type(token))
print(type(clientid))
print(type(chatinfoId))
"""token = json.dumps(token)
print(type(token))"""
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

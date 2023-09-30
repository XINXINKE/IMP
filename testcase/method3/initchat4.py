from testcase.method3.gettokenid2 import SaveTokenid
from common.sendrequest import ApiRequest

"""该方法就是通过调用获得token和其他id的方法 去拿到这些全局变量，而且该方法要引用最基本的发送方法"""
t = SaveTokenid()
token, clientid, chatinfoId = t.save_tokenid()
initchat = ApiRequest()
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
initchat.post_method(url, data, headers)

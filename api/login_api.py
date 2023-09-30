# ：登录接口
import json
import yaml
import requests
import jsonpath

url = "https://customer-inquiry-chat-plus-sit.mercedes-benz.com.cn/api/v1/common/clientLogin"
headers = {
    'modeltype': 'modeld',
    "flag": "2",
    "content-type": "application/json"}
print(type(headers))
data = {
    "channelId": "f8a23acdac834e81acdb58081c24e66a"}
js_data = json.dumps(data)
res = requests.post(url=url, data=js_data, headers=headers)
print(res.status_code)
# print(res)
res = res.json()
print(res)
token = jsonpath.jsonpath(res, "$.data.token")
clientId = jsonpath.jsonpath(res, "$.data.client.id")
clientId = clientId[0]
chatinfoId = jsonpath.jsonpath(res, "$.data.chatInfo.id")
chatinfoId = chatinfoId[0]
print(token)
print(clientId)
print(chatinfoId)

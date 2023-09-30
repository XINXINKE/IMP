import requests
import jsonpath
from common.parser_file import Yamlfile

""" 设置全局变量方法一：登录接口并获取token及各种id 写到yaml文件里 initchat2去调用yaml里面的token和id 在之间又调用了parsefile的写入文件方法 """

url = "https://customer-inquiry-chat-plus-sit.mercedes-benz.com.cn/api/v1/common/clientLogin"
headers = {
    'modeltype': 'modeld',
    "flag": "2",
    "content-type": "application/json"}
data = {
    "channelId": "f8a23acdac834e81acdb58081c24e66a"}
# data = json.dumps(data)  # dumps:将python字典转化成json格式
res = requests.post(url=url, json=data, headers=headers)
res = res.json()  # json():返回响应的json类型的编码内容（如果有的话）
token = jsonpath.jsonpath(res, "$.data.token")[
    0]  # 调用jsonpath模块的jsonpath函数,提取json体里面的token 一般(对象，指定要提取值的路径) 一开始token的值的类型为列表，需要把他调整成字符串，取列表里索引为0的值
clentid = jsonpath.jsonpath(res, "$.data.client.id")[0]  # 调用jsonpath模块的jsonpath函数,提取json体里面的token 一般(对象，指定要提取值的路径)
chatinfoId = jsonpath.jsonpath(res, "$.data.chatInfo.id")[0]  # 调用jsonpath模块的jsonpath函数,提取json体里面的token 一般(对象，指定要提取值的路径)
value = {"token": token, "clientid": clentid, "chatinfoId": chatinfoId}  # 把这些值以字典的格式写入yaml文件
print(value)
Yamlfile.file_writer(r"D:\liukexin\IM0905\code\data\token.yml", value)  # 调用自己定义的库的方法
""" with open(r"token.yml", 'w', encoding="utf - 8") as f:
 # yaml.dump(value, f) """  # 将上面定义的东西写入文件路径中
print(type(token))
print(token)

import requests
import json
import jsonpath

"""方法二：定义一个把token及id设置成全局变量的方法"""


class SaveTokenid():

    def save_tokenid(self):
        url = "https://customer-inquiry-chat-plus-sit.mercedes-benz.com.cn/api/v1/common/clientLogin"
        headers = {
            'modeltype': 'modeld',
            "flag": "2",
            "content-type": "application/json",
            'connection': 'keep-alive'}
        data = {
            "channelId": "f8a23acdac834e81acdb58081c24e66a"}
        data = json.dumps(data)  # dumps:将python字典转化成json
        res = requests.post(url=url, data=data, headers=headers)
        res = res.json()  # json():返回响应的json编码内容（如果有的话）
        token = jsonpath.jsonpath(res, "$.data.token")[0]  # 调用jsonpath模块的jsonpath函数,提取json体里面的token 一般(对象，指定要提取值的路径)
        clientid = jsonpath.jsonpath(res, "$.data.client.id")[
            0]  # 调用jsonpath模块的jsonpath函数,提取json体里面的clientid 一般(对象，指定要提取值的路径)
        chatinfoid = jsonpath.jsonpath(res, "$.data.chatInfo.id")[
            0]  # 调用jsonpath模块的jsonpath函数,提取json体里面的chatinfoId 一般(对象，指定要提取值的路径)
        i = token, clientid, chatinfoid
        return i  # i为元组


if __name__ == '__main__':
    t = SaveTokenid()
    # print(t.save_token())   该输出结果为元组
    token, clientid, chatinfoid = t.save_tokenid()
    print(type(token))

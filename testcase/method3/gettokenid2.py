import jsonpath
from common.sendrequest import ApiRequest

"""方法二-2：定义一个把token及id设置成全局变量的方法,而且该方法要引用最基本的发送方法"""


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
        gettoken = ApiRequest()
        # data = json.dumps(data)  # dumps:将python字典转化成json
        res = gettoken.post_method(url, data, headers)
        print(type(res))
        print(type(jsonpath.jsonpath(res, "$.data.token")))
        token = jsonpath.jsonpath(res, "$.data.token")[0]  # 调用jsonpath模块的jsonpath函数,提取json体里面的token 一般(对象，指定要提取值的路径)
        clientid = jsonpath.jsonpath(res, "$.data.client.id")[
            0]  # 调用jsonpath模块的jsonpath函数,提取json体里面的clientid 一般(对象，指定要提取值的路径)
        chatinfoid = jsonpath.jsonpath(res, "$.data.chatInfo.id")[
            0]  # 调用jsonpath模块的jsonpath函数,提取json体里面的chatinfoId 一般(对象，指定要提取值的路径)
        i = token, clientid, chatinfoid
        return i  # i为元组


if __name__ == '__main__':
    t = SaveTokenid()
    t.save_tokenid()

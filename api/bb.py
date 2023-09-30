import requests
import json

data = {"method": "post",
        "url": "https://customer-inquiry-chat-plus-dev.mercedes-benz.com.cn/api/v1/common/clientLogin",
        "headers": {"modeltype": "modeld", "flag": "2", "content-type": "application/json"},
        "json": {"channelId": {"f8a23acdac834e81acdb58081c24e66a"}}}


class A():

    def post_method(self, **kwargs):
        print(self["url"])
        print(type(self["url"]))


if __name__ == '__main__':
    A.post_method(data)

import requests
from common.get_data import *


# 请求方法
class Apirequest(Get_data):
    @staticmethod
    def send_request(file_path, row):
        url = Get_data.get_url(file_path=file_path, row=row)
        method = Get_data.get_method(file_path=file_path, row=row)
        headers = Get_data.get_headers(file_path=file_path, row=row)
        headers = eval(headers)  # 将字符串转化成字典类型 ，因为下面的headers传的是字典类型的
        # print(headers)
        # print(type(headers))
        data = Get_data.get_json(file_path=file_path, row=row)
        data = eval(data)
        # print(type(data))
        res = requests.request(method=method, url=url, headers=headers, json=data)
        return (res.json())


if __name__ == '__main__':
    Apirequest.send_request(r"D:\liukexin\IM0905\code\data\IM_api.xlsx", 1)

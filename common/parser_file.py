import requests
import jsonpath
import yaml
import json
import os


class Yamlfile():
    """写入文件"""

    @staticmethod
    def file_writer(file_path, value):
        with open(file=file_path, mode='w', encoding="utf - 8") as f:
            yaml.dump(value, f)

    """读文件"""

    @staticmethod
    def file_read(file_path):
        with open(file_path, "r") as f:
            dict = yaml.safe_load(f)
            return dict


if __name__ == '__main__':
    t = Yamlfile()
    t.file_writer(r"D:\liukexin\IM0905\code\data\token.yml",
                  value={"token": 8888888, "clientid": 2, "chatinfoId": 77777777})

"""获取文件绝对路径"""

"""class GetAbsolutePath:
    # def __init__(self):
    def get_absolute_path(self, file_name):
        self.file_name = file_name
        absolute_path = (os.path.abspath(file_name))
        absolute_path.replace("\\", "\\").replace('\t', '\\t')
        print(absolute_path)

        # return absolute_path

if __name__ == '__main__':
    x = GetAbsolutePath()  # 先实例化一个对象哦 先让x这个实例先调用这个类
    x.get_absolute_path("token.yml")  # 再让这个x实例调用这个类方法，传入的对应的参数"""

"""file_path = 'token.yml'

absolute_path = os.path.abspath(file_path)

print(absolute_path)    获取文件的绝对路径"""

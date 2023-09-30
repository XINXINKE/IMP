"""提取全局变量并引用"""
from common.parser_file import Yamlfile


class Extractdata():
    @staticmethod
    def extract_token(file_path):
        dict = Yamlfile.file_read(file_path=file_path)
        token = dict["token"]  # 提取yaml文件中的token参数
        return token

    @staticmethod
    def extract_clientid(file_path):
        dict = Yamlfile.file_read(file_path=file_path)
        clientid = dict["clientid"]  # 提取yaml文件中的clientid参数
        return clientid

    @staticmethod
    def extract_chatinfoId(file_path):
        dict = Yamlfile.file_read(file_path=file_path)
        chatinfoId = dict["chatinfoId"]
        return chatinfoId

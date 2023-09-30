import jsonpath
from common.send_request2 import Apirequest
from common.parser_file import Yamlfile
from common.excel_tool import Excelfile

"""方法一-2：该方法要引用最基本的发送方法，并读取excel里面的数据,然后将参数提取到yaml文件里，并且读取yaml文件里面的参数"""


class Login():
    @staticmethod
    def login(file_path_xlsx, file_path_yaml, row):
        res = Apirequest.send_request(file_path=file_path_xlsx, row=row)
        token = jsonpath.jsonpath(res, "$.data.token")[0]
        clientid = jsonpath.jsonpath(res, "$.data.client.id")[
            0]
        chatinfoid = jsonpath.jsonpath(res, "$.data.chatInfo.id")[
            0]
        value = {"token": token, "clientid": clientid, "chatinfoId": chatinfoid}
        Yamlfile.file_writer(file_path=file_path_yaml, value=value)

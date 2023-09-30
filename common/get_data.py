from common.excel_tool import Excelfile

"""得到excel文件里的data"""


class Get_data():
    @staticmethod  # 是一个静态方法，不用调用实例
    def get_url(file_path, row):
        url = Excelfile.read_excel_col(file_path, 2)  # 读取第2列的所有行数据
        url = url[row - 1]  # 读取第二列从第几行开始的数据
        # print(type(url[0]))
        return (url[0])

    def get_method(file_path, row):
        method = Excelfile.read_excel_col(file_path, 3)
        method = method[row - 1]
        return (method[0])
        # print(type(method[0]))

    def get_headers(file_path, row):
        headers = Excelfile.read_excel_col(file_path, 4)
        headers = headers[row - 1]
        return (headers[0])
        # print(type(headers[0]))

    def get_json(file_path, row):
        json = Excelfile.read_excel_col(file_path, 5)
        json = json[row - 1]
        return (json[0])
        # print(type(json[0]))


if __name__ == '__main__':
    Get_data.get_url(r"/data/IM_api.xlsx", 1)
    #u.get_method(r"D:\liukexin\IM0905\code\data\IM_api.xlsx", 1)
    #u.get_headers(r"D:\liukexin\IM0905\code\data\IM_api.xlsx", 1)

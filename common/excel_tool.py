import pandas as pd
import numpy as np
import json
from pandas import DataFrame
from common.exsts import Extractdata


class Excelfile():
    """读取指定列的所有行数据"""

    @classmethod
    def read_excel_col(cls, file_path, col):
        df = pd.read_excel(file_path)
        data = df.iloc[:, [col]].values
        data = np.array(data)  # 把numpy变成python list列表
        data = data.tolist()
        # print(type(data))
        return (data)

    @classmethod
    def write_excel_col(cls, file_path):
        # token = Extractdata.extract_token()
        # clientid = Extractdata.extract_clientid()
        token = 1
        df = pd.read_excel(file_path)

        df.replace(to_replace=200, value=token)
        df.to_excel(r"D:\liukexin\IM0905\code\data\IM_api.xlsx", index=False)


if __name__ == '__main__':
    u = Excelfile()
    u.write_excel_col(r"D:\liukexin\IM0905\code\data\IM_api.xlsx")

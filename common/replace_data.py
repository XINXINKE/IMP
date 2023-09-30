import requests
from common.exsts import Extractdata
import pandas as pd
import numpy as np


class Replacedata():
    @staticmethod
    def replace_token(file_path):
        token = 1
        df = pd.read_excel(file_path)
        # df.iloc[0] = df.iloc[0].str.replace("1", "aa")
        # data2 = df.iloc[0].isin([200])
        # df.to_excel(r"D:\liukexin\IM0905\code\data\IM_api.xlsx", index=False)
        # df = df.loc[:, "data"]
        data2 = df.loc[:, "headers"].isin(["token0"])
        print(type(df))
        print(data2)


if __name__ == '__main__':
    Replacedata.replace_token(r"D:\liukexin\IM0905\code\data\IM_api.xlsx")

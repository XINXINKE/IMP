"""class只是一个模板而已,定义了一些属性，但是没有实例就相当于没有灵魂"""
"""就像卖手机的，得有价格，品牌，操作系统，厂家这些，而class就是定义手机这个类所都拥有的属性"""
"""self指的是我们物件本身"""
"""定义函数方法的时候，这些参数都不是写死的哦，都是一个大概的名字"""
import requests


class Phone:

    def __init__(self, os, number, is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

    def message(self):
        print("send")

    def calcullate(self, number1, number2):
        return number1 + number2


"""得给这个手机赋值呀"""

apple = Phone("ios", 22, 'i')
apple.message()
print(apple.calcullate(2, 3))

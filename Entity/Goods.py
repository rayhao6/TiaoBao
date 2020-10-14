import datetime

def tid_maker():
    return '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())

class Good:
    goodId = 0
    goodName = ''
    goodNum = 0
    goodPrice = 0
    BulidTime = ''
    goodBrand = ''

    def __init__(self, name, num, price, time, brand):
        self.goodId = tid_maker()
        self.goodName = name
        self.goodNum = num
        self.goodPrice = price
        self.BulidTime = time
        self.goodBrand = brand

    def GetPrice(self):
        return self.goodNum * self.goodPrice




import datetime
import Goods
def tid_maker():
    return '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())

class Order:
    orderId = 0
    orderPrice = 0
    orderPlace = ''
    createdTime = ''
    good = []
    totalNum = 0


    def __init__(self,id, price,place, time, num):
         self.orderId = id
         self.orderPrice = price
         self.orderPlace = place
         self.createdTime = datetime.datetime.now().isoformat()
         self.totalNum = len(self.good)

    def GetPrice(self):
        total = 0
        for i in self.good:
            total += i.price
        return total

    def GetNum(self):
        return len(self.good)

    def AddGood(self, theGood):
        self.good.append(theGood)



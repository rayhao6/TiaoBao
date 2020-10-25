import datetime
import Good
import Customers


class Cart:
    totalPrice = 0
    createdTime = ''
    good = []
    customer = Customers.Customer()
    totalNum = 0


    def __init__(self, place, time, num):
         self.createdTime = datetime.datetime.now().isoformat()
         self.totalNum = len(self.good)
         self.totalPrice = self.GetPrice()

    def GetPrice(self):
        total = 0
        for i in self.good:
            total += i.price
        self.totalPrice = total
        return total

    def GetNum(self):
        return len(self.good)

    def AddGood(self, theGood):
        self.good.append(theGood)


cart = Cart()


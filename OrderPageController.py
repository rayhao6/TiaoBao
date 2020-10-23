import sys
sys.path.append('..')
from Entity.Orders import Order
from Entity.Customers import Customer
class OrderPageController:
    def __init__(self,customer,order):
        self.customer = customer
        self.order = order

    #返回默认地址
    def showPlace(self):
        return self.customer.usualPlace[0]
    
    #返回所有的地址
    def showMorePlace(self):
        return self.customer.usualPlace

    #改变当前订单的收货地址
    def changePlace(self,index):
        self.order.orderPlace = self.customer.usualPlace[index]

    def check(self):
        if self.customer.balance >= self.order.orderPrice:
            self.customer.balance -= self.order.orderPrice
            return True
        else:
            return False
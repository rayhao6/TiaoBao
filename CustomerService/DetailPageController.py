from Goods import Good
from Cart import Cart
class DetailPageController:

    def __init__(self,oneGood,cart):
        self.oneGood = oneGood
        self.cart = cart
    
    def addGood(self,cart,oneGood):
        self.cart.AddGood(oneGood)

#调整good的参数

import sys
sys.path.append('..')
from Entity.Goods import Good
from Entity.Cart import cart
class DetailPageController:

    def __init__(self,oneGood,cart):
        self.oneGood = oneGood
        self.cart = cart
    
    #将此商品添加到购物车中
    def addGood(self,cart,oneGood):
        self.cart.AddGood(oneGood)

#调整good的参数

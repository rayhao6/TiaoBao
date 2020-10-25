import sys
sys.path.append('..')
from Entity.Goods import Good
from Entity.Cart import cart
class DetailPageController:

    def __init__(self,oneGood):
        self.oneGood = oneGood
    
    #将此商品添加到购物车中
    def addGood(self,oneGood):
        cart.AddGood(oneGood)

#调整good的参数

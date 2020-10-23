import sys
sys.path.append('..')
from Entity.Goods import Good
from Entity.Cart import cart

class CartPageController:
    def __init__(self,cart):
        self.cart = cart
    
    #删除购物车中的一个商品
    def deleteGood(self,cart,index):
        del self.cart.good[index]

    #增加某一个商品的数量
    def subGoodNumber(self,cart,index):
        self.cart.good[index].goodNum -= 1
        if self.cart.good[index].goodNum == 0:
            self.deleteGood(cart,index)

    #减少某一个商品的数量
    def addGoodNumber(self,cart,index):
        self.cart.good[index].goodNum += 1
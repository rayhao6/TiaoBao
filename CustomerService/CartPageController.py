from Goods import Good
from Cart import Cart

class CartPageController:
    def __init__(self,cart):
        self.cart = cart
    
    def deleteGood(self,cart,index):
        del self.cart.good[index]

    def subGoodNumber(self,cart,index):
        self.cart.good[index].goodNum -= 1
        if self.cart.good[index].goodNum == 0:
            self.deleteGood(cart,index)


    def addGoodNumber(self,cart,index):
        self.cart.good[index].goodNum += 1



import sys
from Entity.Good import Good
from Entity.Cart import cart
from CustomerService.OpCart import OpCart
sys.path.append('..')


class CartPageController:
    
    # 增加某一个商品的数量
    def subGoodNumber(self, index):
        oneGood = cart.good[index]
        opcart = OpCart(cart)
        opcart.op(oneGood, 1)

    # 减少某一个商品的数量
    def addGoodNumber(self, index):
        oneGood = cart.good[index]
        opcart = OpCart(cart)
        opcart.op(oneGood, -1)

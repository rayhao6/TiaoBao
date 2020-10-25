import sys
from CustomerService.OpCart import OpCart
from Entity.Good import Good
from Entity.Cart import cart
sys.path.append('..')


class DetailPageController:

    def __init__(self, oneGood):
        self.oneGood = oneGood
    
    # 将此商品添加到购物车中
    def addGood(self, oneGood, num):
        opcart = OpCart(cart)
        opcart.op(oneGood, num)

# 调整good的参数

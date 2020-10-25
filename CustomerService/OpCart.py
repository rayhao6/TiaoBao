from MysqlOp import MysqldbHelper
from Entity.Goods import Goods


# 外观模式
class OpCart:

    '''
    示例：
    opcart = OpCart()
    opcart.op(car, 1)  # 添加一个car商品
    opcart.op(car, -1)  # 删除一个car商品
    '''

    def __init__(self, cart):
        self.cart = cart

    # 判断是否存在该商品
    def __exist(self, good):
        for goods in self.cart.good:
            if goods.good == good:
                return True
        return False

    # 返回商品的索引
    def __return_index(self, index, good):
        for goods in self.cart.good:
            if goods.good == good:
                return index
            index += 1

    # 添加或删除操作
    def op(self, good, num):
        mydb = MysqldbHelper()
        table = 'cart'+cart.customer.customerId
        if self.__exist(good):  # 如果商品已经在购物车中，进行数量的修改
            index = self.__return_index(0, good)
            if num + self.cart.good[index].num <= 0:  # 如果最后该商品的个数小于等于0，则删除该商品
                del self.cart.good[index]
                params = {'name': cart.good[index].good.goodName, 'id': cart.good[index].good.goodId}
                mydb.delete(table, params)
            else:
                self.cart.good[index].num += num  # 如果最后该商品的个数大于0，则修改该商品个数
                params = {'name': cart.good[index].good.goodName, 'id': cart.good[index].good.goodId, 'num': cart.good[index].num}
                cond_dict = {'name': cart.good[index].good.goodName, 'id': cart.good[index].good.goodId, 'num': cart.good[index].num+num}
                mydb.update(table, cond_dict, params)
        else:
            if num > 0:  # 如果购物车不存在该商品且num大于0，则放入购物车
                goods = Goods(good, num)
                cart.AddGood(goods)
                params = {'name': good.goodName, 'id': good.goodId, 'num': num}
                mydb.insert(table, params)
            else:
                print("购物车中不存在该商品，无法删减")

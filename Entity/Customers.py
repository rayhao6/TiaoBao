import Orders
import random

class Customer:
    customerId = 0
    phoneNum = ''
    sex = ''
    age = ''
    usualPlace = []
    userName = ''
    realName = ''
    order = []
    def __init__(self, customerId, phoneNum, sex, age, userName, realName):
        self.age = age
        self.sex = sex
        self.phoneNum = phoneNum
        self.realName = realName
        self.userName = userName
        self.customerId = random.randint(10000,99999)

    def AddOrder(self, theOrder):
        self.order.append(theOrder)


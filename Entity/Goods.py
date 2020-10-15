import datetime

def tid_maker():
    return '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())

class Good:
    goodId = 0
    goodName = ''
    goodNum = 0
    goodPrice = 0
    BulidTime = ''
    goodBrand = ''

    def __init__(self, name, num, price, time, brand):
        self.goodId = tid_maker()
        self.goodName = name
        self.goodNum = num
        self.goodPrice = price
        self.BulidTime = time
        self.goodBrand = brand

    def GetPrice(self):
        return self.goodNum * self.goodPrice

class Food(Good):
    taste = ''
    shelfLife = ''
    def __int__(self, taste, shelfLife):
        self.taste = taste
        self.shelfLife = shelfLife

class Snack(Food):
    weight = 0


class Drink(Food):
    volume = ''


class Clothes(Good):
    size = []
    color = []
    material = []
    sex = ''


class Shirt(Clothes):
    collor = ''


class Electronic(Good):
    type = ''
    material = ''
    size = []
    color = []


class Phone(Electronic):
    camera = ''
    battery = ''
    netType = ''


class CPU:
    frequecy = 0
    cores = 0
    threads = 0


class RAM:
    storage = 0
    frequency = 0


class Computer(Electronic):
    CPU = CPU()
    RAM = RAM()

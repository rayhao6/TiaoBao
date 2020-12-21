import datetime
import abc


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

    def __init__(self, taste, shelfLife, name, num, price, time, brand):
        Good.__init__(name, num, price, time, brand)
        self.taste = taste
        self.shelfLife = shelfLife


class Snack(Food):
    weight = 0

    def __init__(self, weight, taste, shelfLife, name, num, price, time, brand):
        Food.__init__(taste, shelfLife, name, num, price, time, brand)
        self.weight = weight


class Drink(Food):
    volume = ''

    def __init__(self, volume, weight, taste, shelfLife, name, num, price, time, brand):
        Food.__init__(weight, taste, shelfLife, name, num, price, time, brand)
        self.volume = volume


class Clothes(Good):
    size = []
    color = []
    material = []
    sex = ''

    def __init__(self, name, num, price, time, brand, size: list, material: list, color: list, sex:str):
        Good.__init__(name, num, price, time, brand)
        self.size = size
        self.material = material
        self.color = color
        self.sex = sex



class Shirt(Clothes):
    collor = ''

    def __init__(self, name, num, price, time, brand, size: list, material: list, color: list, sex: str, collor):
        Clothes.__init__(name, num, price, time, brand, size, material, color, sex)
        self.collor = collor


class Electronic(Good):
    type = ''
    material = ''
    size = []
    color = []

    def __init__(self,name, num, price, time, brand, type: str, material: str, size: list, color: list):
        Good.__init__(name, num, price, time, brand)
        self.type = type
        self.material = material
        self.size = size
        self.color = color


class Phone(Electronic):
    camera = ''
    battery = ''
    netType = ''

    def __init__(self, name, num, price, time, brand, type: str, material: str, size: list, color: list, camera, battery, netType):
        Electronic.__init__(name, num, price, time, brand, type, material, size, color)
        self.camera = camera
        self.netType = netType
        self.battery = battery


class CPU:
    frequency = 0
    cores = 0
    threads = 0

    def __init__(self, name, num, price, time, brand, type: str, material: str, size: list, color: list,
                 frequency, cores, threads):
        Electronic.__init__(name, num, price, time, brand, type, material, size, color)
        self.frequency = frequency
        self.cores = cores
        self.threads = threads


class RAM:
    storage = 0
    frequency = 0

    def __init__(self, name, num, price, time, brand, type: str, material: str, size: list, color: list,
                 frequency, storage):
        Electronic.__init__(name, num, price, time, brand, type, material, size, color)
        self.storage = storage
        self.frequency = frequency


class Computer(Electronic):
    cpu: CPU
    ram: RAM

    def __init__(self, name, num, price, time, brand, type: str, material: str, size: list, color: list,
                 cpu: CPU, ram: RAM):
        Electronic.__init__(name, num, price, time, brand, type, material, size, color)
        self.cpu = cpu
        self.ram = ram

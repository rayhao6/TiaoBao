import Goods
from abc import ABCMeta, abstractmethod, ABC


class AbsFactory:
    @abstractmethod
    def produce(self, name:str):
        pass


class FoodFactory(AbsFactory):
    def produce(self, name:str):
        if name == 'Snack':
            return Goods.Snack()
        if name == 'Drink':
            return Goods.Drink()


class ClotherFactory(AbsFactory):
    def produce(self, name:str):
        if name == 'Shirt':
            return Goods.Shirt()


class ElectricityFactory(AbsFactory):
    def produce(self, name:str):
        if name == 'Phone':
            return Goods.Phone()
        if name == 'Computer':
            return Goods.Computer()








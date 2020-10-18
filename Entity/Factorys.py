import Goods
from abc import ABCMeta, abstractmethod, ABC


class AbsFactory:
    @abstractmethod
    def produce_food(self, name:str):
        pass

    @abstractmethod
    def produce_clothes(self, name:str):
        pass

    def produce_electricity(self, name:str):
        pass


class Factory(AbsFactory):
    def produce_food(self, name:str):
        if name == 'Snack':
            return Goods.Snack()
        if name == 'Drink':
            return Goods.Drink()

    def produce_clothes(self, name:str):
        if name == 'Shirt':
            return Goods.Shirt()

    def produce_electricity(self, name:str):
        if name == 'Phone':
            return Goods.Phone()
        if name == 'Computer':
            return Goods.Computer()








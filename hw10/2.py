a=0
""" Реализовать проект расчёта суммарного расхода ткани на производство одежды 
    Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property"""
from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, information):
        self.information = information

    @abstractmethod
    def calculation(self):
       pass

    def __add__(self, other):
        return self.calculation + other.calculation


class Caat(Clothes):

    @property
    def calculation(self):
        return self.information / 6.5 + 0.5


class Growth(Clothes):

    @property
    def calculation(self):
        return 2 * self.information + 0.3




coat = Caat(45)
growth = Growth(45)

print(coat.calculation)
print(growth.calculation)

print(coat + growth)



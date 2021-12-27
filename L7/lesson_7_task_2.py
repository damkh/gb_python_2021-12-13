"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def fabric(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    def __str__(self):
        return f'{self.fabric}'


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def fabric(self):
        return round(self.v/6.5 + 0.5, 3)

    def __add__(self, other):
        result = Coat(self.v + other.v)
        return result


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def fabric(self):
        return 2 * self.h + 0.3

    def __add__(self, other):
        result = Suit(self.h + other.h)
        return result


my_coat_1 = Coat(3)
print(f'my_coat_1: {my_coat_1}')
my_coat_2 = Coat(5)
print(f'my_coat_2: {my_coat_2}')
my_coat_3 = Coat(1)
print(f'my_coat_3: {my_coat_3}')
print(type(my_coat_1 + my_coat_2 + my_coat_3), my_coat_1 + my_coat_2 + my_coat_3)

my_suit_1 = Suit(5)
print(f'my_suit_1: {my_suit_1}')
my_suit_2 = Suit(3)
print(f'my_suit_2: {my_suit_2}')
print(type(my_suit_1 + my_suit_2), my_suit_1 + my_suit_2)

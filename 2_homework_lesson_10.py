#!/usr/bin/env python3
# Урок 10. Объектно-ориентированное программирование. Продвинутый уровень
# Задание 2
# разбор решения преподавателя
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calculate(self):
        return round((2 * self.param) + 0.3)

coat = Coat(45)
suit = Suit(185)
print(coat.calculate)
print(suit.calculate)

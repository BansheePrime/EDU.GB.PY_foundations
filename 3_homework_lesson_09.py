#!/usr/bin/env python3
# Урок 9. Объектно-ориентированное программирование (ООП)
# Задание 3
# разбор решения преподавателя
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return self._income_wage + self._income_bonus


pos = Position('Alex', 'Alexeev', 'senior', {"wage": 15155.15, "bonus": 14144.14})
print(pos.get_full_name())
print(pos.get_total_income())
#!/usr/bin/env python3
# Урок 9. Объектно-ориентированное программирование (ООП)
# Задание 2
# разбор решения преподавателя
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass

any_road = Road(20, 5000)
print(any_road.road_mass(), 'т')


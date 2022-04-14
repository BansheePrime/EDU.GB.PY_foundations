#!/usr/bin/env python3
# Урок 9. Объектно-ориентированное программирование (ООП)
# Задание 1
# разбор решения преподавателя
from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = (('red', 5), ('yellow'), 2), ('green', 5))

    def running(self):
        '''работа светофора'''
        for color, sec in cycle(self.__color):
            print(color, '(wait {} sec)'.format(sec))
            sleep(sec)

traffic_light = TrafficLight()
traffic_light.running

# for i in range(7, -1, -1):
#     time.sleep(1)
#     print(f'\r{i}', end='')
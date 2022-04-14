#!/usr/bin/env python3
# Урок 9. Объектно-ориентированное программирование (ООП)
# Задание 5
# разбор решения преподавателя

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Ручка пишет')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует')


class Handle(Stationery):
    def draw(self):
        print('Маркер расчерчивает')

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()

#!/usr/bin/env python3
# Урок 9. Объектно-ориентированное программирование (ООП)
# Задание 4
# разбор решения преподавателя
class Car:
    def __init__(self, speed, color, name, dredd):
        self.speed = speed
        self.color = color
        self.name = name
        self.dredd = dredd

    def go(self):
        print('{} going on!'.format(self.name))

    def stop(self):
        print('{} stopped!'.format(self.name))

    def turn(self, direction):
        print('{} is turning towards {}!'.format(self.name, direction))

    def show_speed(self):
        print('Actual speed is: ', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Warning. You going too fast!')

class SportsCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print('Actual speed is: ', self.speed)
        if self.speed > 40:
            print('Warning. You going too fast!')


class PoliceCar(Car):
    pass

sports_car = SportsCar(240, 'Красная', 'Спортивная машина', False)
town_car = TownCar(140, 'Серая', 'Городская машина', False)
work_car = WorkCar(90, 'Жёлтая', 'Рабочая машина', False)
police_car = PoliceCar(210, 'Чёрная', 'Полицейская машина', False)

sports_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sports_car.turn('right')

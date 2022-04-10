#!/usr/bin/env python3
# Урок 8. Декораторы
# Задание 3
# разбор решения преподавателя
from functools import wraps
def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    ''' обязательно импортировать модуль functools'''
    return list(map(lambda x: x ** 3, args))

a = calc_cube(5, 3)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)

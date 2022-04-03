#!/usr/bin/env python3
#
import sys

print(f'Гроссбух пекарни "Мёртвый попугай".  Версия ПО: {sys.argv[0]}')

usefull_data = sys.argv[1]

with open('bakery.csv', 'a+', encoding='utf-8') as file:
    file.write(f'\n{usefull_data};')

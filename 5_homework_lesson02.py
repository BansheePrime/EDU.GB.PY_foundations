#!/usr/bin/env python3
# Урок 2. Некоторые встроенные типы и операции с ними
# Мой шедевр:
# print(f'Цена изделия: {item_price[0].zfill(2)} рублей и {item_price[-1].zfill(2)} копеек', end="")
import random

pricelist = [round(random.uniform(80, 280), 2) for i in range(20)]
readable_up = []
readable_down = []

print('Вывод цен по возрастанию и через запятую, следуя формату "X руб 00 коп": ')
for j in sorted(pricelist):
    item_price = str(j).split(".")
    readable_up.append(f'{item_price[0].zfill(2)} руб {item_price[-1].zfill(2)} коп')

print(*readable_up, sep = ", ")
print()

print('Вывод цен по убыванию: ')
for j in sorted(pricelist, reverse=True):
    item_price = str(j).split(".")
    readable_down.append(f'{item_price[0].zfill(2)} руб {item_price[-1].zfill(2)} коп')

print(*readable_down, sep = ", ")
print()

print(f'Самые дорогие товары в списке по возрастанию: \n{readable_down[5::-1]}')

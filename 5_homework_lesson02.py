#!/usr/bin/env python3
# Урок 2. Некоторые встроенные типы и операции с ними
# Мой шедевр:
# print(f'Цена изделия: {item_price[0].zfill(2)} рублей и {item_price[-1].zfill(2)} копеек', end="")

# Создать список, содержащий цены на товары (10–20 товаров)
import random

pricelist = [round(random.uniform(80, 280), 2) for i in range(20)]
readable_pricelist = []
readable_down = []

# Вывести на экран эти цены через запятую в одну строку,
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули,
# если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

print('Вывод цен через запятую, следуя формату "X руб 00 коп": ')
# for j in sorted(pricelist):
for j in pricelist:
    item_price = str(j).split(".")
    readable_pricelist.append(f'{item_price[0].zfill(2)} руб {item_price[-1].zfill(2)} коп')

print(*readable_pricelist, sep = ", ")
print()

print('Вывод цен по возрастанию без создания списка и с проверкой id: ')
print(id(readable_pricelist))
readable_pricelist.sort()
print(id(readable_pricelist))
print(*readable_pricelist, sep = ", ")

# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).

print('Вывод цен по убыванию: ')
for j in sorted(pricelist, reverse=True):
    item_price = str(j).split(".")
    readable_down.append(f'{item_price[0].zfill(2)} руб {item_price[-1].zfill(2)} коп')

print(*readable_down, sep = ", ")
print()

print(f'Самые дорогие товары в списке по возрастанию: \n{readable_down[5::-1]}')

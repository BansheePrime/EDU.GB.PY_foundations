#!/usr/bin/env python3
# Урок 2. Некоторые встроенные типы и операции с ними
import random

pricelist = [round(random.uniform(80, 280), 2) for i in range(20)]

print('Вывод цен через запятую, следуя формату "руб 00 коп": ')
for j in pricelist:
    item_price = str(j).split(".")
    print(f'{item_price[0].zfill(2)} руб {item_price[-1].zfill(2)} коп', end=", ")

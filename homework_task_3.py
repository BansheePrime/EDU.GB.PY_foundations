#!/usr/bin/env python3
# Slavic declensions

from http.client import NON_AUTHORITATIVE_INFORMATION
from urllib.parse import non_hierarchical


number = int(input('Пожалуйста, введите число от 1 до 100: '))
while 1 < number > 100:
    number = int(input(f'Вы ввели {number}. Я только учусь и пока могу работать только с числами от 1 до 100.\nПопробуйте еще раз: '))
else:
    print(f'Вы ввели число {number}.')
    
nihil_endings = [1, 21, 31, 41, 51, 61, 71, 81, 91]
unus_endings = [2,3,4,22,23,24,32,33,34,42,43,44,52,53,54,62,63,64,72,73,74,82,83,84,92,93,94]

if number in nihil_endings:
    print(f'Можно сказать, что прибыль {number} процент.')
elif number in unus_endings:
    print(f'Можно сказать, что прибыль {number} процента.')
else:
    print(f'Можно сказать, что прибыль {number} процентов.')

print('Вы просили 99 строк? \nПожалуйста...\n')

for i in range(1, 100):
    if i in nihil_endings:
        print(f'{i} процент')
    elif i in unus_endings:
        print(f'{i} процента')
    else:
        print(f'{i} процентов')

print('THE END')

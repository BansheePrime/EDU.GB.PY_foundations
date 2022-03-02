#!/usr/bin/env python3
# Math for mind wipe
# Задание нуждается в переформулировке.
# Прикладываю ДВЕ ВЕРСИИ ответа.

odd_range = range(1, 1001, 2)

for i in odd_range:
    odd_list = list(odd_range)
    power_of_three = [i ** 3 for i in odd_list]

sums_for_division = []

for j in power_of_three:
    summation = 0
    for digit in str(j):
        summation += int(digit)
    sums_for_division.append(summation)

#print(sums_for_division)

first_batch = []

for h in sums_for_division:
    if h % 7 == 0:
        first_batch.append(h)

# print(first_batch)

first_result = sum(first_batch)
print(f'Результат ПЕРВОЙ подзадачи по версии К. Маркса: {first_result}')

seven_teenth = []
for q in power_of_three:
    x = q + 17
    seven_teenth.append(x)

# print(seventeenth)
sums_of_seventeenth = []

for y in seven_teenth:
    divination = 0
    for figit in str(y):
        divination += int(figit)
    sums_of_seventeenth.append(divination)

second_batch = []

for z in sums_of_seventeenth:
    if z % 7 ==0:
        second_batch.append(z)

second_result = sum(second_batch)
print(f'Результат ВТОРОЙ подзадачи по версии К. Маркса: {second_result}')

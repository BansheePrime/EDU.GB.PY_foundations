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

#!/usr/bin/env python3
# Неряшливость формулировки задачи вынуждает обратиться к классикам.
# Версия задания имени Ф. Энгельса

engels_range = range(1, 1001, 2)

for i in engels_range:
        engels_list = list(engels_range)
        power_of_three_engels = [i ** 3 for i in engels_list]

# print(power_of_three_engels)

sums_for_engels = []

for j in power_of_three_engels:
        summation_engels = sum(int(engels) for engels in str(j))
        if summation_engels % 7 == 0:
                sums_for_engels.append(j)

first_engels_batch = sum(sums_for_engels)
print(f'Результат ПЕРВОЙ подзадачи по версии Ф. Энгельса: {first_engels_batch}')
# print(sums_for_engels)
# print(len(sums_for_engels))

seventeenth_engels = []

for foo in power_of_three_engels:
        bar = foo + 17
        seventeenth_engels.append(bar)

# print(seventeenth_engels)

sums_of_seventeen_engels = []

for eggs in seventeenth_engels:
        divination_engels = sum(int(marx) for marx in str(eggs))
        if divination_engels % 7 == 0:
                sums_of_seventeen_engels.append(eggs)

second_engels_batch = sum(sums_of_seventeen_engels)
print(f'Результат ВТОРОЙ подзадачи по версии Ф. Энгельса: {second_engels_batch}')

# Результат ПЕРВОЙ подзадачи по версии К. Маркса: 3437
# Результат ВТОРОЙ подзадачи по версии К. Маркса: 2282
# Результат ПЕРВОЙ подзадачи по версии Ф. Энгельса: 17485588610
# Результат ВТОРОЙ подзадачи по версии Ф. Энгельса: 15392909930

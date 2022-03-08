#!/usr/bin/env python3
# Урок 2. Некоторые встроенные типы и операции с ними
# Сложные манипуляции. Я не знал о startswith и таких возможностях форматирования

original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result_list = []

for i in original_list:
    if i.isdigit():
        result_list.extend(['"', f'{int(i):02}', '"'])
    elif (i.startswith('+') and i[1:].isdigit()):
        result_list.extend(['"', f'{i[0]}{int(i[1:]):02}', '"'])
    else:
        result_list.append(i)

# print(result_list)

finished_exercise = ' '.join(result_list)
print(finished_exercise)

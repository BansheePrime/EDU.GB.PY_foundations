#!/usr/bin/env python3
# Разбор решения преподавателя
import sys

with open('bakery.csv', 'w') as file:
    file.write('5978.5\n8914.3\n7879.12\n1573.74')

edit_index, new_value = sys.argv[1:]
with open('bakery.csv', 'r+') as file:
    temp_file = open('bakery.tmp', 'w+')
    change = False
    for i, line in enumerate(file, 1):
        if i == int(edit_index):
            temp_file.write(f'{new_value}\n')
            change = True
        else:
            temp_file.write(line)
    if not change:
        exit('error')

    temp_file.seek(0)

    file.truncate(0)
    for line in temp_file:
        file.write(line)
    temp_file.close()

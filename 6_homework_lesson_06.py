#!/usr/bin/env python3
#
import sys

operation_lines = []

print(f'Гроссбух пекарни "Мёртвый попугай".  Версия ПО: {sys.argv[0]}')
print('''
Режимы работы ПО:
1 — запуск скрипта без аргументов. Результат: вывод всех записей.
2 — запуск скрипта с одним аргументом-числом. Результат: вывод всех записей с номера, равного этому числу, до конца.
3 — запуск скрипта с двумя аргументами-числами. Результат: вывод записей с номера, равного первому числу, по номер, равный второму числу, включительно.
''')

if len(sys.argv) == 3:
    working_mode = 3
    print(f'Пользователь передал два аргумента. {(str(sys.argv[1:]))}'
          f'\nГроссбух "Мёртвый попугай" работает в режиме 3.'
          f'\nОжидается вывод записей с номера, равного первому числу, по номер, равный второму числу, включительно.')
elif len(sys.argv) == 2:
    working_mode = 2
    print(f'Пользователь передал один аргумент. {str(sys.argv[1:])}'
          f'\nГроссбух "Мёртвый попугай" работает в режиме 2.'
          f'\nОжидается вывод всех записей с номера, равного этому числу, до конца.')
elif len(sys.argv) == 1:
    working_mode = 1
    print(f'Пользователь не передал аргументов.'
          f'\nГроссбух "Мёртвый попугай" работает в режиме 1.'
          f'\nОжидается вывод всех записей.')
else:
    working_mode = 'error'
    print(f'Пользователь передал больше ожидаемого числа аргументов.')
    exit(1)

with open('bakery.csv', 'r', encoding='utf-8') as file:
    lines_number = sum(1 for line in file)
    if working_mode == 3:
        file.seek(0)
        start_line = int(sys.argv[1])
        end_line = int(sys.argv[-1])
        if start_line > 0 and end_line <= lines_number:
            for line in file:
                operation_lines.append(line.replace(';', '').strip())
            print('\n'.join(map(str, operation_lines[start_line - 1:end_line])))
        else:
            print(f'\nВнимание, пользователь!'
                f'\nВведите число больше единицы и меньше или равно числу {lines_number}')

    elif working_mode == 2:
        file.seek(0)
        start_line = int(sys.argv[1])
        if start_line > 0 and start_line < lines_number:
            for line in file:
                operation_lines.append(line.replace(';', '').strip())
            print('\n'.join(map(str, operation_lines[start_line - 1:])))
        else:
            print(f'Введите число меньше числа продаж, которое равно: {lines_number}')
    else:
        file.seek(0)
        for line in file:
            print(line.replace(";", ""), end='')
        print()

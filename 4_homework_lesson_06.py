#!/usr/bin/env python3
# Разбор решения преподавателя
from itertools import zip_longest

with open('user_hobby.txt', 'w', encoding='utf-8') as f:
    with open('users.csv', encoding='utf-8') as users_list:
        with open('hobby.csv', encoding='utf-8') as hobby_list:
            users_lines_quantity = sum(1 for line in users_list)
            hobby_lines_quantity = sum(1 for line in hobby_list)

            if users_lines_quantity < hobby_lines_quantity:
                exit(1)

            users_list.seek(0)
            hobby_list.seek(0)
            for line_users, line_hobbies in zip_longest(users_list, hobby_list):
                f.write(f'{line_users.strip()}: '
                        f'{line_hobbies.strip() if line_hobbies is not None else line_hobbies}\n')

#!/usr/bin/env python3
# Урок 8. Декораторы
# Задание 1

import re

RE_EMAIL = re.compile(r'\b[\w.-]+?@\w+?\.\w+?\b')


def email_parse(email_address):
    """Парсер e-mail"""
    return RE_EMAIL.match(email_address)


if __name__ == '__main__':
    while True:
        email_address = input('Введите адрес для парсинга:\n')
        if email_parse(email_address):
            break
    print(f'Результат:{email_address}')

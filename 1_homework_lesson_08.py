#!/usr/bin/env python3
# Урок 8. Декораторы
# Задание 1
import re
# '\b[\w.-]+?@\w+?\.\w+?\b' - работает в одноязычной среде
# не ловит ошибки вида: 'ааа@ввв.ыыы'
# '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)' нашел в Сети
RE_EMAIL = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')


def email_parse(email_address):
    """Парсер e-mail"""
    if RE_EMAIL.match(email_address) != None:
        result_dict = {}
        email_address = email_address.split('@')
        result_dict.update({email_address[0]: email_address[1]})
    else:
        raise ValueError
    return result_dict


print(email_parse('asd@asd.asd'))
print(email_parse('фыв@фыв.фыв'))
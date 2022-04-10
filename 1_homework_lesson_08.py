#!/usr/bin/env python3
# Урок 8. Декораторы
# Задание 1
import re
# '\b[\w.-]+?@\w+?\.\w+?\b' - работает в одноязычной среде и не ловит ошибки вида: 'ааа@ввв.ыыы'
# '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)' нашел в Сети
# Вид результата: {'username': 'someone', 'domain': 'geekbrains.ru'}

RE_EMAIL = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
# RE_USER = re.compile(r'^([a-zA-Z0-9_.+-]+)@')
# RE_DOMAIN = re.compile(r'@([a-zA-Z0-9-]+\.[a-zA-Z0-9-]+)$')

def email_validation(email_address):
    ''' Валидация email'''
    return RE_EMAIL.match(email_address)

try:
    email_address = 'someone.someone@geekbrains.ru'
    # email_address = 'фыв@фыв.фыв'
    if email_validation(email_address) != None:
        print(f'Продолжим работу с адресом: {email_address}')
        result_dict = {}
        clear_user_name = str(re.findall(r'^([a-zA-Z0-9_.+-]+)@', email_address)).strip('\'[]')
        result_dict.update({'username': clear_user_name})
        clear_domain_name = str(re.findall(r'@([a-zA-Z0-9-]+\.[a-zA-Z0-9-]+)$', email_address)).strip('\'[]')
        result_dict.update({'domain': clear_domain_name})
        print(result_dict)
    else:
        raise ValueError
except ValueError:
    print('Вышла ошибка класса "ValueError"')

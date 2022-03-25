#!/usr/bin/env python3

import requests
import pprint
# Только для того, чтобы напечтать аббревиатуры валют в удобном виде

source_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
data_str = source_str.text
for i in '<?/"=>':
    data_str = data_str.replace(i, '   ')
new_list = []
new_list = data_str.split('  ')
while('' in new_list):
    new_list.remove('')

new_list = [j.strip(' ') for j in new_list]
operational_data = new_list[5]
new_list = new_list[8:]
del new_list[-2:]

currency_abbreviation = new_list[6::18]
currency_nominal = new_list[9::18]
currency_rus_name = new_list[12::18]
currency_value = new_list[15::18]

if len(currency_abbreviation) == len(currency_rus_name) == len(currency_nominal) == len(currency_value):
    print('Ок!')
else:
    print('Ошибка...')

readable_values = zip(currency_rus_name, currency_nominal, currency_value)
readable_dict = dict(zip(currency_abbreviation, readable_values))


def get_list(dict):
    # из словаря извлекаю в список только ключи
    dict_keys = []
    for key in dict.keys():
        dict_keys.append(key)
    return dict_keys

print('Список доступной валюты: ')
pprint.pprint(get_list(readable_dict), compact=tuple)

user_input = input('Пожалуйста, введите аббревиатуру валюты из списка: ')
while user_input.upper() not in get_list(readable_dict):
    user_input = input('Пожалуйста, введите верную аббревиатуру валюты из списка: ')
print(f'Вы выбрали: {user_input.upper()}. \nНам известно, что {operational_data} '
    f'за {list(readable_dict.get(user_input.upper()))[1]} {list(readable_dict.get(user_input.upper()))[0]} '
    f'дают {list(readable_dict.get(user_input.upper()))[2]} рублей.')

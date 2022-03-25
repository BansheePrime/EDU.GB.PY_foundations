#!/usr/bin/env python3

import pprint

source_str = ('<?xml version="1.0" encoding="windows-1251"?><ValCurs Date="25.03.2022" name="Foreign Currency Market"><Valute ID="R01010"><NumCode>036</NumCode><CharCode>AUD</CharCode><Nominal>1</Nominal><Name>Австралийский доллар</Name><Value>71,9575</Value></Valute><Valute ID="R01020A"><NumCode>944</NumCode><CharCode>AZN</CharCode><Nominal>1</Nominal><Name>Азербайджанский манат</Name><Value>56,6375</Value></Valute><Valute ID="R01035"><NumCode>826</NumCode><CharCode>GBP</CharCode><Nominal>1</Nominal><Name>Фунт стерлингов Соединенного королевства</Name><Value>126,6940</Value></Valute><Valute ID="R01060"><NumCode>051</NumCode><CharCode>AMD</CharCode><Nominal>100</Nominal><Name>Армянских драмов</Name><Value>19,5720</Value></Valute><Valute ID="R01090B"><NumCode>933</NumCode><CharCode>BYN</CharCode><Nominal>1</Nominal><Name>Белорусский рубль</Name><Value>30,0594</Value></Valute><Valute ID="R01100"><NumCode>975</NumCode><CharCode>BGN</CharCode><Nominal>1</Nominal><Name>Болгарский лев</Name><Value>53,9371</Value></Valute><Valute ID="R01115"><NumCode>986</NumCode><CharCode>BRL</CharCode><Nominal>1</Nominal><Name>Бразильский реал</Name><Value>19,8947</Value></Valute><Valute ID="R01135"><NumCode>348</NumCode><CharCode>HUF</CharCode><Nominal>100</Nominal><Name>Венгерских форинтов</Name><Value>28,1692</Value></Valute><Valute ID="R01200"><NumCode>344</NumCode><CharCode>HKD</CharCode><Nominal>1</Nominal><Name>Гонконгский доллар</Name><Value>12,2758</Value></Valute><Valute ID="R01215"><NumCode>208</NumCode><CharCode>DKK</CharCode><Nominal>1</Nominal><Name>Датская крона</Name><Value>14,1767</Value></Valute><Valute ID="R01235"><NumCode>840</NumCode><CharCode>USD</CharCode><Nominal>1</Nominal><Name>Доллар США</Name><Value>96,0458</Value></Valute><Valute ID="R01239"><NumCode>978</NumCode><CharCode>EUR</CharCode><Nominal>1</Nominal><Name>Евро</Name><Value>105,4679</Value></Valute><Valute ID="R01270"><NumCode>356</NumCode><CharCode>INR</CharCode><Nominal>10</Nominal><Name>Индийских рупий</Name><Value>12,5760</Value></Valute><Valute ID="R01335"><NumCode>398</NumCode><CharCode>KZT</CharCode><Nominal>100</Nominal><Name>Казахстанских тенге</Name><Value>19,4515</Value></Valute><Valute ID="R01350"><NumCode>124</NumCode><CharCode>CAD</CharCode><Nominal>1</Nominal><Name>Канадский доллар</Name><Value>76,4452</Value></Valute><Valute ID="R01370"><NumCode>417</NumCode><CharCode>KGS</CharCode><Nominal>100</Nominal><Name>Киргизских сомов</Name><Value>97,1747</Value></Valute><Valute ID="R01375"><NumCode>156</NumCode><CharCode>CNY</CharCode><Nominal>1</Nominal><Name>Китайский юань</Name><Value>15,0771</Value></Valute><Valute ID="R01500"><NumCode>498</NumCode><CharCode>MDL</CharCode><Nominal>10</Nominal><Name>Молдавских леев</Name><Value>52,2815</Value></Valute><Valute ID="R01535"><NumCode>578</NumCode><CharCode>NOK</CharCode><Nominal>1</Nominal><Name>Норвежская крона</Name><Value>11,1117</Value></Valute><Valute ID="R01565"><NumCode>985</NumCode><CharCode>PLN</CharCode><Nominal>1</Nominal><Name>Польский злотый</Name><Value>22,2782</Value></Valute><Valute ID="R01585F"><NumCode>946</NumCode><CharCode>RON</CharCode><Nominal>1</Nominal><Name>Румынский лей</Name><Value>21,3123</Value></Valute><Valute ID="R01589"><NumCode>960</NumCode><CharCode>XDR</CharCode><Nominal>1</Nominal><Name>СДР (специальные права заимствования)</Name><Value>132,4039</Value></Valute><Valute ID="R01625"><NumCode>702</NumCode><CharCode>SGD</CharCode><Nominal>1</Nominal><Name>Сингапурский доллар</Name><Value>70,7207</Value></Valute><Valute ID="R01670"><NumCode>972</NumCode><CharCode>TJS</CharCode><Nominal>10</Nominal><Name>Таджикских сомони</Name><Value>79,3537</Value></Valute><Valute ID="R01700J"><NumCode>949</NumCode><CharCode>TRY</CharCode><Nominal>10</Nominal><Name>Турецких лир</Name><Value>64,7257</Value></Valute><Valute ID="R01710A"><NumCode>934</NumCode><CharCode>TMT</CharCode><Nominal>1</Nominal><Name>Новый туркменский манат</Name><Value>27,4417</Value></Valute><Valute ID="R01717"><NumCode>860</NumCode><CharCode>UZS</CharCode><Nominal>10000</Nominal><Name>Узбекских сумов</Name><Value>83,3910</Value></Valute><Valute ID="R01720"><NumCode>980</NumCode><CharCode>UAH</CharCode><Nominal>10</Nominal><Name>Украинских гривен</Name><Value>32,6684</Value></Valute><Valute ID="R01760"><NumCode>203</NumCode><CharCode>CZK</CharCode><Nominal>10</Nominal><Name>Чешских крон</Name><Value>42,7024</Value></Valute><Valute ID="R01770"><NumCode>752</NumCode><CharCode>SEK</CharCode><Nominal>1</Nominal><Name>Шведская крона</Name><Value>10,1959</Value></Valute><Valute ID="R01775"><NumCode>756</NumCode><CharCode>CHF</CharCode><Nominal>1</Nominal><Name>Швейцарский франк</Name><Value>103,1530</Value></Valute><Valute ID="R01810"><NumCode>710</NumCode><CharCode>ZAR</CharCode><Nominal>10</Nominal><Name>Южноафриканских рэндов</Name><Value>65,6015</Value></Valute><Valute ID="R01815"><NumCode>410</NumCode><CharCode>KRW</CharCode><Nominal>1000</Nominal><Name>Вон Республики Корея</Name><Value>78,8068</Value></Valute><Valute ID="R01820"><NumCode>392</NumCode><CharCode>JPY</CharCode><Nominal>100</Nominal><Name>Японских иен</Name><Value>78,8068</Value></Valute></ValCurs>')
data_str = source_str
for i in '<?/"=>':
    data_str = data_str.replace(i, '   ')
new_list = []
new_list = data_str.split('  ')
while('' in new_list):
    new_list.remove('')

new_list = [j.strip(' ') for j in new_list]
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
# print('*** ***')

readable_values = zip(currency_rus_name, currency_nominal, currency_value)
readable_dict = dict(zip(currency_abbreviation, readable_values))
# print(readable_dict)
# print('*** ***')


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
print(f'Вы выбрали: {user_input.upper()}.')
      # f'Нам известно, что это {readable_dict.get(user_input.upper())}')
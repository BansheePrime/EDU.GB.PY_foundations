#!/usr/bin/env python3
# Урок 3. Функции. Словари
import random
some_number = int(input('Введите желаемое количество шуток: '))
repeat_key = int(input('По умолчанию мы верим в вашу смелость. Если вы боитесь повторов введите цифру "0": ') or 1)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

if repeat_key == 0 and some_number > len(nouns):
    print(f'\nПозвольте уточнить. Вы выбрали {some_number} шуток без повторов.')
    print('Штатный генератор "Петросян 3.0" в бесплатной версии ограничен пятью вариантами.')
    print('Рекомендуем рассмотреть приобретение DLC "Большой... словарь" за $19.99.')
    some_number = 5
else:
    repeat_key = 1


def get_jokes(some_number, repeat_key):
    '''
    Генератор шуток по спискам слов "Петросян 3.0"
    :param some_number: количество шуток
    :param repeat_key: допустимы или нет повторы слов
    :return: anekdot.ru
    '''
    i = 0
    joker = []
    if repeat_key == 0 and some_number < len(nouns):
        for i in range(some_number):
            a = random.choice(nouns)
            nouns.remove(a)
            b = random.choice(adverbs)
            adverbs.remove(b)
            c = random.choice(adjectives)
            adjectives.remove(c)
            joke = (f'{a} {b} {c}')
            i += 1
            joker.append(joke)
    else:
        for i in range(some_number):
            joke = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
            i += 1
            joker.append(joke)
    return print(joker)


get_jokes(some_number, repeat_key)

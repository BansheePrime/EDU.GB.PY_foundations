#!/usr/bin/env python3
# Урок 3. Функции. Словари
import random
some_number = int(input('Введите желаемое количество шуток: '))

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(some_number):
    '''
    Генератор шуток по спискам слов
    :param words: количество шуток
    :return: anekdot.ru
    '''
    i = 0
    joker = []
    for i in range(some_number):
        joke = (f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
        i += 1
        joker.append(joke)
    return print(joker)

get_jokes(some_number)

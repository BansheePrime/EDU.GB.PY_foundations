#!/usr/bin/env python3
# Урок 3. Функции. Словари
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(some_number):
    '''
    Генератор шуток по спискам слов
    :param words: количество шуток
    :return: anekdot.ru
    '''

    joke = {random.choice(nouns)} {random.choice(adverbs)} {random.choice(adverbs)}
    return print(joke)

get_jokes()
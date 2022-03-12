#!/usr/bin/env python3
# Урок 3. Функции. Словари

dictionary_words = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
word_input = input('Введите, пожалуйста, словом число от 0 до 10 на английском языке: ')


def num_translate():
    # Перевод числительных на английский язык с учетом регистра
    if word_input.istitle():
        return print(f'\"{dictionary_words.get(word_input.lower(), None).capitalize()}\"')
    else:
        return print(f'\"{dictionary_words.get(word_input, None)}\"')


num_translate()
